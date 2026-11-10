"""Marketplace tests: no client-supplied ownership, no self applications."""
from decimal import Decimal

from django.contrib.auth import get_user_model
from django.db import IntegrityError, transaction
from rest_framework.test import APITestCase

from apps.accounts.models import Employer, Worker
from .models import Offer, Proposal

User = get_user_model()
PASSWORD = "Valid-Test-Password_374!"


class MarketplaceApiTests(APITestCase):
    def setUp(self):
        self.owner = User.objects.create_user(
            username="owner", name="Owner Demo", email="owner@example.test",
            phone="+258841000001", password=PASSWORD,
        )
        self.worker_user = User.objects.create_user(
            username="worker", name="Worker Demo", email="worker@example.test",
            phone="+258841000002", password=PASSWORD,
        )
        self.other = User.objects.create_user(
            username="other", name="Other Demo", email="other@example.test",
            phone="+258841000003", password=PASSWORD,
        )
        self.employer = Employer.objects.create(
            user=self.owner, company_name="Empresa Exemplo", address="Maputo"
        )
        self.worker = Worker.objects.create(
            user=self.worker_user, skills="Django, React", experience="3 anos"
        )
        self.offer_payload = {
            "title": "Desenvolvimento de portal",
            "description": "Criar um portal de serviços para uma empresa local.",
            "category": "Desenvolvimento Web",
            "required_skills": ["Django", "React"],
            "budget": "25000.00",
            "location": "Maputo",
        }
        self.proposal_payload = {
            "description": "Desenvolverei o portal Django e React em duas fases.",
            "proposed_amount": "23000.00",
            "timeline_days": 21,
        }

    def make_offer(self):
        return Offer.objects.create(
            employer=self.employer,
            title=self.offer_payload["title"],
            description=self.offer_payload["description"],
            category=self.offer_payload["category"],
            required_skills=self.offer_payload["required_skills"],
            budget=Decimal("25000.00"),
            location="Maputo",
        )

    def test_anonymous_can_read_active_offers_but_cannot_publish(self):
        offer = self.make_offer()
        list_response = self.client.get("/api/marketplace/offers/")
        self.assertEqual(list_response.status_code, 200)
        self.assertEqual(list_response.data[0]["id"], offer.pk)
        self.assertEqual(list_response.data[0]["employer_user_id"], self.owner.pk)
        self.assertNotIn("email", list_response.data[0])
        unauthorized = self.client.post("/api/marketplace/offers/", self.offer_payload, format="json")
        self.assertEqual(unauthorized.status_code, 401)

    def test_employer_can_publish_and_server_sets_owner(self):
        self.client.force_authenticate(user=self.owner)
        data = {**self.offer_payload, "employer_user_id": self.other.id}
        response = self.client.post("/api/marketplace/offers/", data, format="json")
        self.assertEqual(response.status_code, 201, response.data)
        self.assertEqual(response.data["employer_user_id"], self.owner.id)
        self.assertEqual(Offer.objects.get(pk=response.data["id"]).employer_id, self.employer.pk)

    def test_user_without_employer_profile_cannot_publish(self):
        self.client.force_authenticate(user=self.worker_user)
        response = self.client.post(
            "/api/marketplace/offers/", self.offer_payload, format="json"
        )
        self.assertEqual(response.status_code, 403)
        self.assertEqual(Offer.objects.count(), 0)

    def test_offer_validation_rejects_blank_or_duplicate_skills(self):
        self.client.force_authenticate(user=self.owner)
        data = {**self.offer_payload, "required_skills": ["Django", "django"]}
        self.assertEqual(self.client.post(
            "/api/marketplace/offers/", data, format="json"
        ).status_code, 400)
        data = {**self.offer_payload, "budget": "0"}
        self.assertEqual(self.client.post(
            "/api/marketplace/offers/", data, format="json"
        ).status_code, 400)

    def test_worker_can_apply_and_view_only_own_proposals(self):
        offer = self.make_offer()
        self.client.force_authenticate(user=self.worker_user)
        result = self.client.post(
            f"/api/marketplace/offers/{offer.pk}/proposals/",
            self.proposal_payload, format="json",
        )
        self.assertEqual(result.status_code, 201, result.data)
        self.assertEqual(result.data["offer_id"], offer.id)
        self.assertEqual(result.data["worker_user_id"], self.worker_user.id)
        mine = self.client.get("/api/marketplace/proposals/mine/")
        self.assertEqual(mine.status_code, 200)
        self.assertEqual(len(mine.data), 1)
        self.client.force_authenticate(user=self.other)
        self.assertEqual(self.client.get("/api/marketplace/proposals/mine/").data, [])

    def test_rn02_dual_profile_owner_cannot_apply_to_own_offer(self):
        offer = self.make_offer()
        Worker.objects.create(
            user=self.owner, skills="Python", experience="3 anos"
        )
        self.client.force_authenticate(user=self.owner)
        response = self.client.post(
            f"/api/marketplace/offers/{offer.pk}/proposals/",
            self.proposal_payload, format="json",
        )
        self.assertEqual(response.status_code, 403, response.data)
        self.assertEqual(Proposal.objects.count(), 0)

    def test_duplicate_proposals_rejected_in_api_and_database(self):
        offer = self.make_offer()
        self.client.force_authenticate(user=self.worker_user)
        path = f"/api/marketplace/offers/{offer.id}/proposals/"
        self.assertEqual(
            self.client.post(path, self.proposal_payload, format="json").status_code,
            201,
        )
        self.assertEqual(
            self.client.post(path, self.proposal_payload, format="json").status_code,
            409,
        )
        with self.assertRaises(IntegrityError):
            with transaction.atomic():
                Proposal.objects.create(
                    offer=offer, worker=self.worker,
                    description=self.proposal_payload["description"],
                    proposed_amount=Decimal("23000"),
                    timeline_days=12,
                )
        self.assertEqual(Proposal.objects.count(), 1)

    def test_only_employer_can_list_proposals_for_their_offer(self):
        offer = self.make_offer()
        Proposal.objects.create(
            offer=offer, worker=self.worker,
            description=self.proposal_payload["description"],
            proposed_amount=Decimal("23000"), timeline_days=12,
        )
        endpoint = f"/api/marketplace/offers/{offer.pk}/proposals/"
        self.client.force_authenticate(user=self.other)
        self.assertEqual(self.client.get(endpoint).status_code, 403)
        self.client.force_authenticate(user=self.owner)
        response = self.client.get(endpoint)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_only_owner_may_edit_and_close_offer(self):
        offer = self.make_offer()
        endpoint = f"/api/marketplace/offers/{offer.pk}/"
        self.client.force_authenticate(user=self.other)
        self.assertEqual(self.client.patch(endpoint, {"title": "Changed"}).status_code, 403)
        self.assertEqual(
            self.client.post(f"{endpoint}close/").status_code, 403
        )
        self.client.force_authenticate(user=self.owner)
        new_title = "Novo título da oportunidade"
        self.assertEqual(self.client.patch(
            endpoint, {"title": new_title}
        ).status_code, 200)
        self.assertEqual(self.client.post(f"{endpoint}close/").status_code, 200)
        offer.refresh_from_db()
        self.assertEqual(offer.status, Offer.Status.CLOSED)
        self.client.force_authenticate(user=None)
        self.assertEqual(self.client.get(endpoint).status_code, 404)
        self.assertEqual(self.client.get("/api/marketplace/offers/").data, [])

    def test_closed_offer_does_not_accept_applications(self):
        offer = self.make_offer()
        offer.status = Offer.Status.CLOSED
        offer.save()
        self.client.force_authenticate(user=self.worker_user)
        result = self.client.post(
            f"/api/marketplace/offers/{offer.pk}/proposals/",
            self.proposal_payload, format="json",
        )
        self.assertEqual(result.status_code, 409)

    def test_offer_with_proposals_cannot_be_silently_rewritten(self):
        offer = self.make_offer()
        Proposal.objects.create(
            offer=offer, worker=self.worker,
            description=self.proposal_payload["description"],
            proposed_amount=Decimal("23000"), timeline_days=12,
        )
        self.client.force_authenticate(user=self.owner)
        response = self.client.patch(
            f"/api/marketplace/offers/{offer.pk}/",
            {"budget": "1.00"}, format="json",
        )
        self.assertEqual(response.status_code, 409)
        offer.refresh_from_db()
        self.assertEqual(offer.budget, Decimal("25000.00"))

    def test_worker_profile_is_required_to_submit_proposal(self):
        offer = self.make_offer()
        self.client.force_authenticate(user=self.other)
        response = self.client.post(
            f"/api/marketplace/offers/{offer.pk}/proposals/",
            self.proposal_payload, format="json",
        )
        self.assertEqual(response.status_code, 403)
