"""D51: actual Django/DRF vertical slice regression tests (not the D49 reference model)."""
from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase

from apps.accounts.models import Employer, Worker
from apps.marketplace.models import Opportunity, Proposal
from apps.contracts.models import AgreementAcceptance, AgreementVersion, Engagement


User = get_user_model()


class ContractVerticalSliceTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.employer = User.objects.create_user(
            username="client_d51", password="TestOnly!234", name="Client",
            email="client_d51@example.test", phone="+258841234567"
        )
        cls.worker = User.objects.create_user(
            username="worker_d51", password="TestOnly!234", name="Worker",
            email="worker_d51@example.test", phone="+258821234567"
        )
        cls.worker2 = User.objects.create_user(
            username="worker2_d51", password="TestOnly!234", name="Worker 2",
            email="worker2_d51@example.test", phone="+258831234567"
        )
        cls.outsider = User.objects.create_user(
            username="outsider_d51", password="TestOnly!234", name="Outsider",
            email="outsider_d51@example.test", phone="+258851234567"
        )
        cls.employer_profile = Employer.objects.create(
            user=cls.employer, company_name="Test Ltd", address="Maputo"
        )
        cls.worker_profile = Worker.objects.create(
            user=cls.worker, skills="Django", experience="2 anos"
        )
        cls.worker2_profile = Worker.objects.create(
            user=cls.worker2, skills="React", experience="3 anos"
        )

    def authenticate(self, user):
        self.client.force_authenticate(user=user)

    def opportunity(self, *, published=True):
        self.authenticate(self.employer)
        made = self.client.post("/api/marketplace/opportunities/", {
            "title": "Desenvolver website", "description": "Site institucional",
        }, format="json")
        self.assertEqual(made.status_code, 201, getattr(made, "data", None))
        opportunity_id = made.data["id"]
        if published:
            response = self.client.post(
                f"/api/marketplace/opportunities/{opportunity_id}/publish/"
            )
            self.assertEqual(response.status_code, 200)
        return opportunity_id

    def proposal(self, opportunity_id, worker=None):
        worker = worker or self.worker
        self.authenticate(worker)
        response = self.client.post(
            f"/api/marketplace/opportunities/{opportunity_id}/proposals/",
            {"description": "Executo este serviço"}, format="json"
        )
        self.assertEqual(response.status_code, 201, getattr(response, "data", None))
        return response.data["id"]

    def engagement(self):
        opportunity_id = self.opportunity()
        proposal_id = self.proposal(opportunity_id)
        self.authenticate(self.employer)
        response = self.client.post(
            f"/api/marketplace/proposals/{proposal_id}/accept/"
        )
        self.assertEqual(response.status_code, 201, getattr(response, "data", None))
        return response.data["engagement_id"]

    def propose_version(self, engagement_id, user=None, payload=None):
        self.authenticate(user or self.employer)
        response = self.client.post(
            f"/api/contracts/engagements/{engagement_id}/agreements/",
            payload or {"scope": "Website + documentação", "amount": "25000.00"},
            format="json"
        )
        self.assertEqual(response.status_code, 201, getattr(response, "data", None))
        return response.data["version_id"]

    def accept(self, engagement_id, version_id, user):
        self.authenticate(user)
        fingerprint = AgreementVersion.objects.get(pk=version_id).content_fingerprint
        return self.client.post(
            f"/api/contracts/engagements/{engagement_id}/agreements/{version_id}/accept/",
            {"content_fingerprint": fingerprint},
            format="json",
        )

    def test_anonymous_cannot_list_opportunities(self):
        self.client.force_authenticate(user=None)
        response = self.client.get("/api/marketplace/opportunities/")
        self.assertEqual(response.status_code, 401)

    def test_only_employer_profile_can_create_opportunity(self):
        self.authenticate(self.worker)
        response = self.client.post(
            "/api/marketplace/opportunities/",
            {"title": "Tarefa", "description": "Descrição"}, format="json"
        )
        self.assertEqual(response.status_code, 403)

    def test_draft_not_public_and_owner_can_publish(self):
        pk = self.opportunity(published=False)
        self.authenticate(self.worker)
        items = self.client.get("/api/marketplace/opportunities/").data
        self.assertFalse(any(item["id"] == pk for item in items))
        self.authenticate(self.employer)
        self.assertTrue(any(item["id"] == pk for item in self.client.get("/api/marketplace/opportunities/").data))
        self.assertEqual(
            self.client.post(f"/api/marketplace/opportunities/{pk}/publish/").status_code,
            200,
        )
        self.authenticate(self.worker)
        self.assertTrue(any(item["id"] == pk for item in self.client.get("/api/marketplace/opportunities/").data))

    def test_non_owner_cannot_publish(self):
        pk = self.opportunity(published=False)
        self.authenticate(self.worker)
        self.assertEqual(
            self.client.post(f"/api/marketplace/opportunities/{pk}/publish/").status_code,
            403,
        )
        self.assertEqual(Opportunity.objects.get(pk=pk).status, Opportunity.Status.DRAFT)

    def test_cannot_submit_proposal_to_draft(self):
        pk = self.opportunity(published=False)
        self.authenticate(self.worker)
        r = self.client.post(
            f"/api/marketplace/opportunities/{pk}/proposals/",
            {"description": "Posso fazer"}, format="json"
        )
        self.assertEqual(r.status_code, 409)

    def test_worker_profile_required_to_submit_proposal(self):
        pk = self.opportunity()
        self.authenticate(self.outsider)
        r = self.client.post(
            f"/api/marketplace/opportunities/{pk}/proposals/",
            {"description": "Sou candidato"}, format="json"
        )
        self.assertEqual(r.status_code, 403)

    def test_same_user_can_have_both_profiles_but_cannot_self_contract(self):
        Worker.objects.create(user=self.employer, skills="React", experience="2 anos")
        pk = self.opportunity()
        self.authenticate(self.employer)
        r = self.client.post(
            f"/api/marketplace/opportunities/{pk}/proposals/",
            {"description": "Tentativa de auto-contratação"}, format="json"
        )
        self.assertEqual(r.status_code, 403)
        self.assertEqual(Proposal.objects.count(), 0)

    def test_proposal_duplicate_rejected(self):
        pk = self.opportunity()
        self.proposal(pk)
        self.authenticate(self.worker)
        r = self.client.post(
            f"/api/marketplace/opportunities/{pk}/proposals/",
            {"description": "Duplicado"}, format="json"
        )
        self.assertEqual(r.status_code, 409)
        self.assertEqual(Proposal.objects.count(), 1)

    def test_worker_cannot_accept_own_proposal(self):
        pk = self.opportunity()
        proposal_id = self.proposal(pk)
        self.authenticate(self.worker)
        r = self.client.post(f"/api/marketplace/proposals/{proposal_id}/accept/")
        self.assertEqual(r.status_code, 403)
        self.assertFalse(Engagement.objects.exists())

    def test_accepting_proposal_creates_pending_engagement_and_closes_opportunity(self):
        pk = self.opportunity()
        proposal_id = self.proposal(pk)
        alternate_id = self.proposal(pk, self.worker2)
        self.authenticate(self.employer)
        r = self.client.post(f"/api/marketplace/proposals/{proposal_id}/accept/")
        self.assertEqual(r.status_code, 201)
        self.assertEqual(r.data["engagement_status"], Engagement.Status.PENDING_AGREEMENT)
        self.assertEqual(Opportunity.objects.get(pk=pk).status, Opportunity.Status.CLOSED)
        self.assertEqual(Proposal.objects.get(pk=alternate_id).status, Proposal.Status.REJECTED)
        self.assertEqual(Engagement.objects.get(pk=r.data["engagement_id"]).proposal_id, proposal_id)

    def test_cannot_accept_second_proposal_after_first(self):
        pk = self.opportunity()
        first = self.proposal(pk)
        second = self.proposal(pk, self.worker2)
        self.authenticate(self.employer)
        self.assertEqual(self.client.post(f"/api/marketplace/proposals/{first}/accept/").status_code, 201)
        self.assertEqual(self.client.post(f"/api/marketplace/proposals/{second}/accept/").status_code, 409)
        self.assertEqual(Engagement.objects.count(), 1)

    def test_non_party_cannot_read_engagement(self):
        engagement_id = self.engagement()
        self.authenticate(self.outsider)
        r = self.client.get(f"/api/contracts/engagements/{engagement_id}/")
        self.assertEqual(r.status_code, 403)

    def test_initial_version_only_party_can_propose(self):
        engagement_id = self.engagement()
        self.authenticate(self.outsider)
        r = self.client.post(
            f"/api/contracts/engagements/{engagement_id}/agreements/",
            {"scope": "Escopo", "amount": "1000.00"}, format="json"
        )
        self.assertEqual(r.status_code, 403)
        self.assertFalse(AgreementVersion.objects.exists())

    def test_terms_must_have_amount_or_price_after_diagnosis(self):
        engagement_id = self.engagement()
        self.authenticate(self.worker)
        for payload in [
            {"scope": "Escopo"},
            {"scope": "Escopo", "price_after_diagnosis": True, "amount": "200.00"},
            {"scope": "Escopo", "amount": "-1"},
        ]:
            with self.subTest(payload=payload):
                r = self.client.post(
                    f"/api/contracts/engagements/{engagement_id}/agreements/",
                    payload, format="json"
                )
                self.assertEqual(r.status_code, 400)
        self.assertFalse(AgreementVersion.objects.exists())

    def test_price_after_diagnosis_is_allowed(self):
        engagement_id = self.engagement()
        vid = self.propose_version(engagement_id, self.worker, {
            "scope": "Diagnóstico primeiro", "price_after_diagnosis": True
        })
        version = AgreementVersion.objects.get(pk=vid)
        self.assertTrue(version.price_after_diagnosis)
        self.assertIsNone(version.amount)

    def test_duplicate_initial_version_rejected(self):
        engagement_id = self.engagement()
        self.propose_version(engagement_id)
        self.authenticate(self.worker)
        r = self.client.post(
            f"/api/contracts/engagements/{engagement_id}/agreements/",
            {"scope": "Segunda v1", "amount": "1000"}, format="json"
        )
        self.assertEqual(r.status_code, 409)
        self.assertEqual(AgreementVersion.objects.count(), 1)

    def test_one_acceptance_does_not_activate_contract(self):
        eid = self.engagement()
        vid = self.propose_version(eid)
        r = self.accept(eid, vid, self.employer)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.data["engagement_status"], Engagement.Status.PENDING_AGREEMENT)
        self.assertEqual(AgreementAcceptance.objects.count(), 1)

    def test_bilateral_acceptance_activates_contract_and_records_distinct_actors(self):
        eid = self.engagement()
        vid = self.propose_version(eid)
        self.assertEqual(self.accept(eid, vid, self.worker).status_code, 200)
        r = self.accept(eid, vid, self.employer)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.data["engagement_status"], Engagement.Status.ACTIVE)
        self.assertEqual(r.data["agreement_status"], AgreementVersion.Status.ACCEPTED)
        self.assertEqual(set(r.data["accepted_by"]), {self.worker.id, self.employer.id})
        view = self.client.get(f"/api/contracts/engagements/{eid}/")
        self.assertEqual(view.status_code, 200)
        self.assertEqual(view.data["versions"][0]["status"], AgreementVersion.Status.ACCEPTED)
        self.assertEqual(AgreementAcceptance.objects.count(), 2)

    def test_duplicate_acceptance_rejected(self):
        eid = self.engagement()
        vid = self.propose_version(eid)
        self.assertEqual(self.accept(eid, vid, self.worker).status_code, 200)
        self.assertEqual(self.accept(eid, vid, self.worker).status_code, 409)
        self.assertEqual(AgreementAcceptance.objects.count(), 1)

    def test_outsider_cannot_accept_agreement(self):
        eid = self.engagement()
        vid = self.propose_version(eid)
        r = self.accept(eid, vid, self.outsider)
        self.assertEqual(r.status_code, 403)
        self.assertEqual(AgreementAcceptance.objects.count(), 0)

    def test_acceptance_fails_for_wrong_engagement_version_pair(self):
        eid = self.engagement()
        vid = self.propose_version(eid)
        second = self.engagement()
        self.authenticate(self.worker)
        r = self.client.post(
            f"/api/contracts/engagements/{second}/agreements/{vid}/accept/"
        )
        self.assertEqual(r.status_code, 404)

    def test_tampered_fingerprint_rejected(self):
        eid = self.engagement()
        vid = self.propose_version(eid)
        AgreementVersion.objects.filter(pk=vid).update(scope="Outro escopo")
        r = self.accept(eid, vid, self.worker)
        self.assertEqual(r.status_code, 409)
        self.assertEqual(AgreementAcceptance.objects.count(), 0)

    def test_active_engagement_rejects_reopening_initial_agreement(self):
        eid = self.engagement()
        vid = self.propose_version(eid)
        self.accept(eid, vid, self.worker)
        self.accept(eid, vid, self.employer)
        self.authenticate(self.employer)
        r = self.client.post(
            f"/api/contracts/engagements/{eid}/agreements/",
            {"scope": "Tentar reabrir", "amount": "2000"}, format="json"
        )
        self.assertEqual(r.status_code, 409)
        self.assertEqual(AgreementVersion.objects.count(), 1)
