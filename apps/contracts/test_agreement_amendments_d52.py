"""D52: DRF API tests for amendments, rejection and agreement integrity."""
from django.contrib.auth import get_user_model
from django.db import IntegrityError, transaction
from rest_framework.test import APITestCase

from apps.accounts.models import Employer, Worker
from apps.marketplace.models import Opportunity, Proposal
from apps.contracts.models import AgreementVersion, AgreementAcceptance, Engagement


User = get_user_model()


class AgreementAmendmentsTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.employer = User.objects.create_user(
            username="employer_d52", password="Test-Only!123", name="Employer",
            email="employer_d52@example.test", phone="+258841234567",
        )
        cls.worker = User.objects.create_user(
            username="worker_d52", password="Test-Only!123", name="Worker",
            email="worker_d52@example.test", phone="+258821234567",
        )
        cls.other = User.objects.create_user(
            username="other_d52", password="Test-Only!123", name="Other",
            email="other_d52@example.test", phone="+258831234567",
        )
        cls.employer_profile = Employer.objects.create(
            user=cls.employer, company_name="Empresa D52", address="Maputo",
        )
        cls.worker_profile = Worker.objects.create(
            user=cls.worker, skills="Python", experience="3 anos",
        )
        cls.opportunity = Opportunity.objects.create(
            employer=cls.employer_profile,
            title="Desenvolver portal",
            description="Um portal de serviços",
            status=Opportunity.Status.CLOSED,
        )
        cls.proposal = Proposal.objects.create(
            opportunity=cls.opportunity,
            worker=cls.worker_profile,
            description="Execução do trabalho",
            status=Proposal.Status.ACCEPTED,
        )
        cls.engagement = Engagement.objects.create(proposal=cls.proposal)

    def login(self, user):
        self.client.force_authenticate(user=user)

    def agreement_url(self):
        return f"/api/contracts/engagements/{self.engagement.pk}/agreements/"

    def accept_url(self, version_id):
        return f"{self.agreement_url()}{version_id}/accept/"

    def reject_url(self, version_id):
        return f"{self.agreement_url()}{version_id}/reject/"

    def detail(self, actor=None):
        self.login(actor or self.worker)
        response = self.client.get(f"/api/contracts/engagements/{self.engagement.pk}/")
        self.assertEqual(response.status_code, 200, response.data)
        return response.data

    def propose(self, actor, scope="Acordo inicial", amount="15000.00", diagnosis=False):
        self.login(actor)
        payload = {"scope": scope, "price_after_diagnosis": diagnosis}
        if amount is not None:
            payload["amount"] = amount
        response = self.client.post(self.agreement_url(), payload, format="json")
        self.assertEqual(response.status_code, 201, response.data)
        return AgreementVersion.objects.get(pk=response.data["version_id"])

    def consent(self, actor, version, *, fingerprint=None):
        self.login(actor)
        response = self.client.post(self.accept_url(version.pk), {
            "content_fingerprint": fingerprint if fingerprint is not None
            else version.content_fingerprint,
        }, format="json")
        return response

    def reject(self, actor, version, reason="Condições não aceites", *, fingerprint=None):
        self.login(actor)
        return self.client.post(self.reject_url(version.pk), {
            "content_fingerprint": fingerprint if fingerprint is not None
            else version.content_fingerprint,
            "reason": reason,
        }, format="json")

    def activate_initial(self):
        v1 = self.propose(self.employer)
        self.assertEqual(self.consent(self.employer, v1).status_code, 200)
        self.assertEqual(self.consent(self.worker, v1).status_code, 200)
        self.engagement.refresh_from_db()
        self.assertEqual(self.engagement.status, Engagement.Status.ACTIVE)
        v1.refresh_from_db()
        self.assertEqual(v1.status, AgreementVersion.Status.ACCEPTED)
        return v1

    def test_acceptance_requires_explicit_fingerprint(self):
        v1 = self.propose(self.employer)
        self.login(self.worker)
        response = self.client.post(self.accept_url(v1.pk), {}, format="json")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(AgreementAcceptance.objects.count(), 0)

    def test_acceptance_rejects_stale_fingerprint(self):
        v1 = self.propose(self.employer)
        response = self.consent(self.worker, v1, fingerprint="0" * 64)
        self.assertEqual(response.status_code, 409)
        self.assertEqual(AgreementAcceptance.objects.count(), 0)

    def test_first_acceptance_keeps_pending_until_both_accept(self):
        v1 = self.propose(self.employer)
        response = self.consent(self.worker, v1)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["engagement_status"], Engagement.Status.PENDING_AGREEMENT)
        self.assertIsNone(response.data["current_agreement_version_id"])

    def test_revision_proposed_does_not_supersede_current_agreement(self):
        v1 = self.activate_initial()
        v2 = self.propose(self.worker, scope="Acordo ajustado", amount="25000.00")
        self.assertEqual(v2.version, 2)
        self.assertEqual(v2.status, AgreementVersion.Status.PROPOSED)
        v1.refresh_from_db()
        self.assertEqual(v1.status, AgreementVersion.Status.ACCEPTED)
        data = self.detail()
        self.assertEqual(data["current_agreement_version_id"], v1.pk)
        self.assertEqual(data["status"], Engagement.Status.ACTIVE)

    def test_first_revision_acceptance_does_not_change_current(self):
        v1 = self.activate_initial()
        v2 = self.propose(self.worker, scope="Revisão", amount="30000.00")
        response = self.consent(self.worker, v2)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["current_agreement_version_id"], v1.pk)
        self.assertEqual(AgreementVersion.objects.get(pk=v1.pk).status, AgreementVersion.Status.ACCEPTED)
        self.assertEqual(AgreementVersion.objects.get(pk=v2.pk).status, AgreementVersion.Status.PROPOSED)

    def test_bilateral_acceptance_promotes_v2_and_supersedes_v1(self):
        v1 = self.activate_initial()
        v2 = self.propose(self.worker, scope="Revisão de escopo", amount="23000.00")
        self.assertEqual(self.consent(self.worker, v2).status_code, 200)
        response = self.consent(self.employer, v2)
        self.assertEqual(response.status_code, 200, response.data)
        self.assertEqual(response.data["current_agreement_version_id"], v2.pk)
        v1.refresh_from_db()
        v2.refresh_from_db()
        self.engagement.refresh_from_db()
        self.assertEqual(v1.status, AgreementVersion.Status.SUPERSEDED)
        self.assertEqual(v2.status, AgreementVersion.Status.ACCEPTED)
        self.assertEqual(self.engagement.status, Engagement.Status.ACTIVE)
        self.assertEqual(AgreementVersion.objects.filter(status="ACCEPTED").count(), 1)

    def test_rejected_revision_preserves_prior_v1_and_rejection_provenance(self):
        v1 = self.activate_initial()
        v2 = self.propose(self.worker, scope="Revisão rejeitada", amount="20000.00")
        self.assertEqual(self.consent(self.worker, v2).status_code, 200)
        response = self.reject(self.employer, v2, reason="Preço não aceite")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["current_agreement_version_id"], v1.pk)
        v1.refresh_from_db()
        v2.refresh_from_db()
        self.assertEqual(v1.status, AgreementVersion.Status.ACCEPTED)
        self.assertEqual(v2.status, AgreementVersion.Status.REJECTED)
        self.assertEqual(v2.rejected_by_id, self.employer.pk)
        self.assertIsNotNone(v2.rejected_at)
        self.assertEqual(v2.rejection_reason, "Preço não aceite")
        self.assertEqual(v2.acceptances.count(), 1)

    def test_proponent_cannot_reject_own_proposal(self):
        self.activate_initial()
        v2 = self.propose(self.worker, scope="Revisão", amount="21000.00")
        response = self.reject(self.worker, v2)
        self.assertEqual(response.status_code, 403)
        self.assertEqual(AgreementVersion.objects.get(pk=v2.pk).status, AgreementVersion.Status.PROPOSED)

    def test_outsider_cannot_reject(self):
        self.activate_initial()
        v2 = self.propose(self.worker, scope="Revisão", amount="21000.00")
        response = self.reject(self.other, v2)
        self.assertEqual(response.status_code, 403)

    def test_reject_fails_for_stale_fingerprint(self):
        self.activate_initial()
        v2 = self.propose(self.worker, scope="Revisão", amount="21000.00")
        response = self.reject(self.employer, v2, fingerprint="f" * 64)
        self.assertEqual(response.status_code, 409)
        self.assertEqual(AgreementVersion.objects.get(pk=v2.pk).status, AgreementVersion.Status.PROPOSED)

    def test_rejection_requires_reason(self):
        self.activate_initial()
        v2 = self.propose(self.worker, scope="Revisão", amount="21000.00")
        response = self.reject(self.employer, v2, reason="")
        self.assertEqual(response.status_code, 400)

    def test_only_one_pending_revision_at_a_time(self):
        self.activate_initial()
        self.propose(self.worker, scope="Revisão", amount="21000.00")
        self.login(self.employer)
        response = self.client.post(self.agreement_url(), {
            "scope": "Segunda revisão simultânea", "amount": "24000.00",
        }, format="json")
        self.assertEqual(response.status_code, 409)
        self.assertEqual(AgreementVersion.objects.count(), 2)

    def test_after_rejecting_v2_can_propose_v3(self):
        v1 = self.activate_initial()
        v2 = self.propose(self.worker, scope="Revisão 2", amount="22000.00")
        self.assertEqual(self.reject(self.employer, v2).status_code, 200)
        v3 = self.propose(self.employer, scope="Revisão 3", amount="24000.00")
        self.assertEqual(v3.version, 3)
        self.assertEqual(AgreementVersion.objects.get(pk=v1.pk).status, AgreementVersion.Status.ACCEPTED)
        self.assertEqual(AgreementVersion.objects.get(pk=v2.pk).status, AgreementVersion.Status.REJECTED)

    def test_cannot_accept_rejected_version(self):
        self.activate_initial()
        v2 = self.propose(self.worker, scope="Revisão", amount="21000.00")
        self.assertEqual(self.reject(self.employer, v2).status_code, 200)
        response = self.consent(self.worker, v2)
        self.assertEqual(response.status_code, 409)

    def test_cannot_reject_already_accepted_version(self):
        v1 = self.activate_initial()
        response = self.reject(self.worker, v1)
        self.assertEqual(response.status_code, 409)

    def test_duplicate_acceptance_of_v2_is_rejected(self):
        self.activate_initial()
        v2 = self.propose(self.worker, scope="Revisão", amount="21000.00")
        self.assertEqual(self.consent(self.worker, v2).status_code, 200)
        self.assertEqual(self.consent(self.worker, v2).status_code, 409)

    def test_other_user_cannot_propose_revision(self):
        self.activate_initial()
        self.login(self.other)
        response = self.client.post(self.agreement_url(), {
            "scope": "Revisão por estranho", "amount": "100.00",
        }, format="json")
        self.assertEqual(response.status_code, 403)

    def test_revision_price_after_diagnosis(self):
        self.activate_initial()
        v2 = self.propose(self.worker, scope="Só diagnóstico", amount=None, diagnosis=True)
        self.assertTrue(v2.price_after_diagnosis)
        self.assertIsNone(v2.amount)

    def test_rejected_initial_version_may_be_replaced_while_pending(self):
        v1 = self.propose(self.employer)
        self.assertEqual(self.reject(self.worker, v1).status_code, 200)
        self.engagement.refresh_from_db()
        self.assertEqual(self.engagement.status, Engagement.Status.PENDING_AGREEMENT)
        v2 = self.propose(self.worker, scope="Novas condições", amount="16000.00")
        self.assertEqual(v2.version, 2)
        self.assertEqual(self.consent(self.worker, v2).status_code, 200)
        self.assertEqual(self.consent(self.employer, v2).status_code, 200)
        self.engagement.refresh_from_db()
        self.assertEqual(self.engagement.status, Engagement.Status.ACTIVE)
        self.assertEqual(AgreementVersion.objects.get(pk=v1.pk).status, AgreementVersion.Status.REJECTED)

    def test_superseded_agreement_cannot_be_accepted(self):
        v1 = self.activate_initial()
        v2 = self.propose(self.worker, scope="Revisão", amount="21000.00")
        self.consent(self.worker, v2)
        self.consent(self.employer, v2)
        response = self.consent(self.worker, v1)
        self.assertEqual(response.status_code, 409)

    def test_tampered_persisted_content_cannot_be_accepted(self):
        self.activate_initial()
        v2 = self.propose(self.worker, scope="Revisão", amount="21000.00")
        AgreementVersion.objects.filter(pk=v2.pk).update(scope="Termos alterados sem versão")
        response = self.consent(self.employer, v2)
        self.assertEqual(response.status_code, 409)

    def test_unique_pending_constraint_at_database_level(self):
        self.activate_initial()
        v2 = self.propose(self.worker, scope="Revisão", amount="21000.00")
        with self.assertRaises(IntegrityError):
            with transaction.atomic():
                AgreementVersion.objects.create(
                    engagement=self.engagement, version=3,
                    scope="Proposta concorrente", amount="22000.00",
                    price_after_diagnosis=False,
                    proposed_by=self.employer,
                    content_fingerprint="0" * 64,
                )
        self.assertEqual(AgreementVersion.objects.filter(status="PROPOSED").count(), 1)
        self.assertEqual(AgreementVersion.objects.get(pk=v2.pk).status, AgreementVersion.Status.PROPOSED)

    def test_unique_current_constraint_at_database_level(self):
        self.activate_initial()
        v2 = self.propose(self.worker, scope="Revisão", amount="21000.00")
        with self.assertRaises(IntegrityError):
            with transaction.atomic():
                AgreementVersion.objects.filter(pk=v2.pk).update(status="ACCEPTED")
        self.assertEqual(AgreementVersion.objects.filter(status="ACCEPTED").count(), 1)

    def test_detail_preserves_version_history_after_rejection(self):
        v1 = self.activate_initial()
        v2 = self.propose(self.worker, scope="Revisão", amount="22000.00")
        self.reject(self.employer, v2, reason="Prazo não adequado")
        history = self.detail()
        self.assertEqual(history["current_agreement_version_id"], v1.pk)
        self.assertEqual([v["status"] for v in history["versions"]], [
            AgreementVersion.Status.ACCEPTED,
            AgreementVersion.Status.REJECTED,
        ])
        self.assertEqual(history["versions"][1]["rejection_reason"], "Prazo não adequado")
        self.assertFalse(history["versions"][1]["is_current"])
