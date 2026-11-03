"""D55: worker-owned proposal states, authorization, and durable read model."""
from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase

from apps.accounts.models import Employer, Worker
from apps.marketplace.models import Opportunity, Proposal

User = get_user_model()


class OwnedProposalStateTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        def make(username, phone):
            return User.objects.create_user(
                username=username, name=username, email=f"{username}@example.test",
                phone=phone, password="TestOnly!D55",
            )
        cls.employer = make("employer_d55", "+258841234567")
        cls.worker = make("worker_d55", "+258821234567")
        cls.other_worker = make("other_worker_d55", "+258831234567")
        cls.employer_profile = Employer.objects.create(
            user=cls.employer, company_name="D55 Ltd", address="Maputo"
        )
        cls.worker_profile = Worker.objects.create(
            user=cls.worker, skills="Django", experience="2 anos"
        )
        cls.other_profile = Worker.objects.create(
            user=cls.other_worker, skills="React", experience="4 anos"
        )
        cls.open = Opportunity.objects.create(
            employer=cls.employer_profile, title="Portal aberto",
            description="Trabalho aberto", status=Opportunity.Status.OPEN
        )
        cls.closed = Opportunity.objects.create(
            employer=cls.employer_profile, title="Portal fechado",
            description="Trabalho fechado", status=Opportunity.Status.CLOSED
        )
        cls.submitted = Proposal.objects.create(
            opportunity=cls.open, worker=cls.worker_profile,
            description="Proposta própria D55", status=Proposal.Status.SUBMITTED
        )
        cls.accepted = Proposal.objects.create(
            opportunity=cls.closed, worker=cls.worker_profile,
            description="Aceite D55", status=Proposal.Status.ACCEPTED
        )
        cls.other_proposal = Proposal.objects.create(
            opportunity=cls.open, worker=cls.other_profile,
            description="Informação confidencial de outra conta",
            status=Proposal.Status.SUBMITTED
        )

    def test_anonymous_cannot_read_owned_proposals(self):
        response = self.client.get("/api/marketplace/proposals/mine/")
        self.assertEqual(response.status_code, 401)

    def test_authenticated_worker_sees_only_own_proposals(self):
        self.client.force_authenticate(user=self.worker)
        response = self.client.get("/api/marketplace/proposals/mine/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(
            {row["id"] for row in response.data}, {self.submitted.pk, self.accepted.pk}
        )
        self.assertNotIn("Informação confidencial de outra conta", str(response.data))
        for row in response.data:
            self.assertNotIn("worker_user_id", row)
            self.assertNotIn("worker_name", row)
            self.assertNotIn("email", row)
            self.assertNotIn("phone", row)

    def test_closed_opportunity_proposal_still_visible_with_status(self):
        self.client.force_authenticate(user=self.worker)
        rows = self.client.get("/api/marketplace/proposals/mine/").data
        closed = next(x for x in rows if x["id"] == self.accepted.pk)
        self.assertEqual(closed["status"], Proposal.Status.ACCEPTED)
        self.assertEqual(closed["opportunity_status"], Opportunity.Status.CLOSED)
        self.assertEqual(closed["opportunity_title"], "Portal fechado")

    def test_other_worker_does_not_see_first_workers_proposals(self):
        self.client.force_authenticate(user=self.other_worker)
        rows = self.client.get("/api/marketplace/proposals/mine/").data
        self.assertEqual([row["id"] for row in rows], [self.other_proposal.pk])
        self.assertNotIn("Aceite D55", str(rows))

    def test_employer_without_worker_profile_gets_empty_list(self):
        self.client.force_authenticate(user=self.employer)
        response = self.client.get("/api/marketplace/proposals/mine/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, [])

    def test_dual_profile_does_not_expose_other_workers_submissions(self):
        Worker.objects.create(user=self.employer, skills="Django", experience="5 anos")
        self.client.force_authenticate(user=self.employer)
        self.assertEqual(self.client.get("/api/marketplace/proposals/mine/").data, [])

    def test_status_is_read_from_database_after_transition(self):
        self.client.force_authenticate(user=self.worker)
        Proposal.objects.filter(pk=self.submitted.pk).update(status=Proposal.Status.REJECTED)
        rows = self.client.get("/api/marketplace/proposals/mine/").data
        found = next(x for x in rows if x["id"] == self.submitted.pk)
        self.assertEqual(found["status"], Proposal.Status.REJECTED)

    def test_worker_cannot_read_employer_only_proposal_list(self):
        self.client.force_authenticate(user=self.worker)
        response = self.client.get(
            f"/api/marketplace/opportunities/{self.open.pk}/proposals/"
        )
        self.assertEqual(response.status_code, 403)

    def test_endpoint_is_read_only(self):
        self.client.force_authenticate(user=self.worker)
        response = self.client.post(
            "/api/marketplace/proposals/mine/", {"status": "ACCEPTED"}, format="json"
        )
        self.assertEqual(response.status_code, 405)
        self.assertEqual(
            Proposal.objects.get(pk=self.submitted.pk).status,
            Proposal.Status.SUBMITTED,
        )
