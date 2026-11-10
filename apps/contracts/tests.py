"""API regressions for RF13/RF14 server-side agreement invariants."""
from decimal import Decimal

from django.contrib.auth import get_user_model
from django.db import IntegrityError, transaction
from rest_framework.test import APITestCase

from apps.accounts.models import Employer, Worker
from apps.marketplace.models import Offer, Proposal
from .models import AgreementApproval, AgreementVersion, Contract

User = get_user_model()
PASSWORD = "Valid-Test-Password_374!"


class AgreementApiTests(APITestCase):
    def setUp(self):
        self.employer_user = User.objects.create_user(
            username="company", name="Empresa Exemplo", email="company@example.test",
            phone="+258841234561", password=PASSWORD,
        )
        self.worker_user = User.objects.create_user(
            username="worker", name="Ana Exemplo", email="worker@example.test",
            phone="+258841234562", password=PASSWORD,
        )
        self.outsider = User.objects.create_user(
            username="other", name="Outro Utilizador", email="other@example.test",
            phone="+258841234563", password=PASSWORD,
        )
        self.employer = Employer.objects.create(
            user=self.employer_user, company_name="Empresa Exemplo", address="Maputo"
        )
        self.worker = Worker.objects.create(
            user=self.worker_user, skills="Django, React", experience="3 anos"
        )
        self.offer = Offer.objects.create(
            employer=self.employer, title="Portal de Serviços TI",
            description="Construção de portal com login, oportunidades e relatórios.",
            category="Desenvolvimento Web", required_skills=["Django"],
            budget=Decimal("25000.00"), location="Maputo",
        )
        self.proposal = Proposal.objects.create(
            offer=self.offer, worker=self.worker,
            description="Construirei o portal com testes de aceitação.",
            proposed_amount=Decimal("23000.00"), timeline_days=21,
        )

    def terms(self, budget="23000.00"):
        advance = Decimal(budget) / 4
        final = Decimal(budget) - advance
        return {
            "title": "Portal de Serviços TI",
            "scope": "Construção de portal de serviços e contactos para empresas de TI.",
            "deliverables": "Código-fonte, testes de aceitação e documentação completa.",
            "acceptance_criteria": "Fluxos de login, pesquisa, proposta e notificação aprovados.",
            "budget": budget,
            "start_date": "2026-11-11",
            "end_date": "2026-12-20",
            "payment_conditions": [
                {
                    "id": "advance", "stage": "ADVANCE", "amount": str(advance),
                    "method": "M-Pesa", "moment": "Depois de ambas as partes aprovarem",
                },
                {
                    "id": "final", "stage": "FINAL", "amount": str(final),
                    "method": "Transferência Bancária",
                    "moment": "Após aceitação formal da entrega final",
                },
            ],
        }

    def accept(self):
        self.client.force_authenticate(user=self.employer_user)
        response = self.client.post(
            f"/api/contracts/from-proposal/{self.proposal.id}/"
        )
        self.assertEqual(response.status_code, 201, response.data)
        return response.data["contract"]["id"], response.data["draft"]["id"]

    def publish(self, version_id, terms=None, actor=None):
        self.client.force_authenticate(user=actor or self.employer_user)
        self.assertEqual(self.client.patch(
            f"/api/contracts/versions/{version_id}/",
            {"terms": terms or self.terms()}, format="json"
        ).status_code, 200)
        response = self.client.post(
            f"/api/contracts/versions/{version_id}/submit/"
        )
        self.assertEqual(response.status_code, 200, response.data)
        return response.data

    def approve(self, version_id, user):
        self.client.force_authenticate(user=user)
        return self.client.post(f"/api/contracts/versions/{version_id}/approve/")

    def activate(self):
        contract_id, v1_id = self.accept()
        self.publish(v1_id)
        first = self.approve(v1_id, self.employer_user)
        self.assertEqual(first.status_code, 200, first.data)
        second = self.approve(v1_id, self.worker_user)
        self.assertEqual(second.status_code, 200, second.data)
        return contract_id, v1_id

    def test_acceptance_creates_pending_contract_and_unsigned_v1_draft(self):
        contract_id, version_id = self.accept()
        contract = Contract.objects.get(id=contract_id)
        version = AgreementVersion.objects.get(id=version_id)
        self.assertEqual(contract.status, Contract.Status.PENDING)
        self.assertIsNone(contract.start_date)
        self.assertEqual(version.status, AgreementVersion.Status.DRAFT)
        self.assertEqual(version.number, 1)
        self.assertEqual(version.approvals.count(), 0)
        self.assertTrue(version.events.filter(action="CREATED").exists())
        self.proposal.refresh_from_db()
        self.offer.refresh_from_db()
        self.assertEqual(self.proposal.status, Proposal.Status.ACCEPTED)
        self.assertEqual(self.offer.status, Offer.Status.CLOSED)

    def test_only_offer_owner_can_accept_and_only_once(self):
        self.client.force_authenticate(user=self.worker_user)
        self.assertEqual(self.client.post(
            f"/api/contracts/from-proposal/{self.proposal.id}/"
        ).status_code, 403)
        contract_id, _ = self.accept()
        self.assertTrue(Contract.objects.filter(id=contract_id).exists())
        self.assertEqual(self.client.post(
            f"/api/contracts/from-proposal/{self.proposal.id}/"
        ).status_code, 409)
        self.assertEqual(Contract.objects.count(), 1)

    def test_nonselected_proposals_are_rejected_after_acceptance(self):
        another_worker = User.objects.create_user(
            username="worker_two", name="Outra Trabalhadora",
            email="second@example.test", phone="+258841234564",
            password=PASSWORD,
        )
        alternate = Worker.objects.create(
            user=another_worker, skills="React", experience="2 anos"
        )
        other_proposal = Proposal.objects.create(
            offer=self.offer, worker=alternate,
            description="Implementação alternativa deste projecto.",
            proposed_amount=Decimal("21000"), timeline_days=30,
        )
        self.accept()
        other_proposal.refresh_from_db()
        self.assertEqual(other_proposal.status, Proposal.Status.REJECTED)

    def test_contract_and_history_not_visible_to_unrelated_user(self):
        contract_id, version_id = self.accept()
        self.client.force_authenticate(user=self.outsider)
        self.assertEqual(self.client.get(
            f"/api/contracts/{contract_id}/"
        ).status_code, 403)
        self.assertEqual(self.client.get(
            f"/api/contracts/{contract_id}/versions/"
        ).status_code, 403)
        self.assertEqual(self.client.post(
            f"/api/contracts/versions/{version_id}/approve/"
        ).status_code, 403)
        self.assertEqual(self.client.get("/api/contracts/mine/").data, [])
        self.client.force_authenticate(user=self.worker_user)
        self.assertEqual(self.client.get(
            f"/api/contracts/{contract_id}/"
        ).status_code, 200)

    def test_author_can_edit_draft_but_other_party_cannot(self):
        contract_id, version_id = self.accept()
        self.client.force_authenticate(user=self.worker_user)
        res = self.client.patch(
            f"/api/contracts/versions/{version_id}/",
            {"terms": self.terms()}, format="json",
        )
        self.assertEqual(res.status_code, 409)
        self.client.force_authenticate(user=self.employer_user)
        res = self.client.patch(
            f"/api/contracts/versions/{version_id}/",
            {"terms": self.terms()}, format="json",
        )
        self.assertEqual(res.status_code, 200)
        self.assertEqual(AgreementVersion.objects.get(
            id=version_id
        ).terms["budget"], "23000.00")

    def test_incomplete_or_inconsistent_terms_cannot_be_published(self):
        _, version_id = self.accept()
        self.client.force_authenticate(user=self.employer_user)
        self.assertEqual(self.client.post(
            f"/api/contracts/versions/{version_id}/submit/"
        ).status_code, 400)
        bad = self.terms()
        bad["payment_conditions"][0]["amount"] = "1000.00"
        self.assertEqual(self.client.patch(
            f"/api/contracts/versions/{version_id}/",
            {"terms": bad}, format="json",
        ).status_code, 200)
        self.assertEqual(self.client.post(
            f"/api/contracts/versions/{version_id}/submit/"
        ).status_code, 400)
        self.assertEqual(
            AgreementVersion.objects.get(id=version_id).status,
            AgreementVersion.Status.DRAFT,
        )
        bad = self.terms()
        bad["end_date"] = "2026-02-31"
        self.client.patch(f"/api/contracts/versions/{version_id}/",
                          {"terms": bad}, format="json")
        self.assertEqual(self.client.post(
            f"/api/contracts/versions/{version_id}/submit/"
        ).status_code, 400)

    def test_one_approval_does_not_activate_contract_or_change_budget(self):
        contract_id, version_id = self.accept()
        self.publish(version_id)
        res = self.approve(version_id, self.employer_user)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.data["status"], AgreementVersion.Status.PENDING_APPROVAL)
        self.assertEqual(res.data["approvals"][0]["user_id"], self.employer_user.id)
        self.assertEqual(Contract.objects.get(id=contract_id).status, Contract.Status.PENDING)
        self.assertEqual(self.approve(version_id, self.employer_user).status_code, 409)

    def test_two_independent_approvals_activate_exact_same_version(self):
        contract_id, version_id = self.activate()
        contract = Contract.objects.get(id=contract_id)
        self.assertEqual(contract.status, Contract.Status.ACTIVE)
        self.assertEqual(contract.start_date.isoformat(), "2026-11-11")
        self.assertEqual(contract.budget, Decimal("23000.00"))
        version = AgreementVersion.objects.get(id=version_id)
        self.assertEqual(version.status, AgreementVersion.Status.ACTIVE)
        self.assertEqual(version.approvals.count(), 2)
        self.assertTrue(version.events.filter(action="ACTIVATED").exists())

    def test_published_terms_cannot_be_mutated_with_patch(self):
        _, version_id = self.accept()
        self.publish(version_id)
        self.client.force_authenticate(user=self.employer_user)
        response = self.client.patch(
            f"/api/contracts/versions/{version_id}/",
            {"terms": self.terms("30000.00")}, format="json",
        )
        self.assertEqual(response.status_code, 409)
        self.assertEqual(
            AgreementVersion.objects.get(id=version_id).terms["budget"],
            "23000.00",
        )

    def test_amendment_remains_inactive_until_both_approve(self):
        contract_id, original_id = self.activate()
        self.client.force_authenticate(user=self.worker_user)
        revised = self.client.post(f"/api/contracts/{contract_id}/amend/", {
            "reason": "Adicionar um módulo de relatórios e alterar o valor",
        })
        self.assertEqual(revised.status_code, 201, revised.data)
        v2 = revised.data["id"]
        updated = self.terms("24000.00")
        updated["scope"] += " Inclui relatórios adicionais e revisão do alcance."
        self.publish(v2, terms=updated, actor=self.worker_user)
        self.assertEqual(self.approve(v2, self.worker_user).status_code, 200)
        contract = Contract.objects.get(id=contract_id)
        self.assertEqual(contract.budget, Decimal("23000.00"))
        self.assertEqual(AgreementVersion.objects.get(
            id=original_id
        ).status, AgreementVersion.Status.ACTIVE)
        self.assertEqual(self.approve(v2, self.employer_user).status_code, 200)
        contract.refresh_from_db()
        self.assertEqual(contract.budget, Decimal("24000.00"))
        original = AgreementVersion.objects.get(id=original_id)
        self.assertEqual(original.status, AgreementVersion.Status.SUPERSEDED)
        self.assertEqual(original.terms["budget"], "23000.00")
        self.assertEqual(AgreementVersion.objects.get(id=v2).number, 2)

    def test_rejected_amendment_does_not_change_active_contract(self):
        contract_id, original_id = self.activate()
        self.client.force_authenticate(user=self.worker_user)
        response = self.client.post(f"/api/contracts/{contract_id}/amend/", {
            "reason": "Alterar as datas de entrega do trabalho",
        })
        v2_id = response.data["id"]
        self.publish(v2_id, actor=self.worker_user)
        self.client.force_authenticate(user=self.employer_user)
        rejected = self.client.post(
            f"/api/contracts/versions/{v2_id}/reject/",
            {"reason": "Prazo proposto não foi acordado por ambas as partes."},
        )
        self.assertEqual(rejected.status_code, 200)
        self.assertEqual(rejected.data["status"], AgreementVersion.Status.REJECTED)
        self.assertEqual(
            AgreementVersion.objects.get(id=original_id).status,
            AgreementVersion.Status.ACTIVE,
        )
        self.assertEqual(Contract.objects.get(id=contract_id).budget, Decimal("23000.00"))

    def test_rejected_initial_version_can_be_renegotiated(self):
        contract_id, v1 = self.accept()
        self.publish(v1)
        self.client.force_authenticate(user=self.worker_user)
        self.assertEqual(self.client.post(
            f"/api/contracts/versions/{v1}/reject/",
            {"reason": "Os critérios de aceitação estão incompletos."},
        ).status_code, 200)
        new = self.client.post(
            f"/api/contracts/{contract_id}/renegotiate/",
            {"reason": "Clarificar o âmbito e a documentação do projecto"},
        )
        self.assertEqual(new.status_code, 201, new.data)
        self.assertEqual(new.data["number"], 2)
        self.assertEqual(new.data["status"], AgreementVersion.Status.DRAFT)
        self.assertEqual(AgreementVersion.objects.filter(contract_id=contract_id).count(), 2)
        self.assertEqual(Contract.objects.get(id=contract_id).status, Contract.Status.PENDING)

    def test_unauthorized_completion_and_premature_completion_rejected(self):
        contract_id, v1 = self.accept()
        self.client.force_authenticate(user=self.employer_user)
        self.assertEqual(self.client.post(
            f"/api/contracts/{contract_id}/complete/"
        ).status_code, 409)
        self.publish(v1)
        self.approve(v1, self.employer_user)
        self.assertEqual(self.client.post(
            f"/api/contracts/{contract_id}/complete/"
        ).status_code, 409)
        self.approve(v1, self.worker_user)
        self.assertEqual(self.client.post(
            f"/api/contracts/{contract_id}/complete/"
        ).status_code, 403)
        self.client.force_authenticate(user=self.employer_user)
        response = self.client.post(f"/api/contracts/{contract_id}/complete/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["status"], Contract.Status.COMPLETED)
        self.assertEqual(self.client.post(
            f"/api/contracts/{contract_id}/complete/"
        ).status_code, 409)

    def test_database_rejects_duplicate_active_agreements(self):
        contract_id, _ = self.activate()
        existing = AgreementVersion.objects.get(
            contract_id=contract_id, status=AgreementVersion.Status.ACTIVE
        )
        with self.assertRaises(IntegrityError):
            with transaction.atomic():
                AgreementVersion.objects.create(
                    contract_id=contract_id, number=7,
                    created_by=self.employer_user, status=AgreementVersion.Status.ACTIVE,
                    reason="Duplicado indevido", terms=existing.terms,
                )
        self.assertEqual(AgreementVersion.objects.filter(
            contract_id=contract_id, status=AgreementVersion.Status.ACTIVE
        ).count(), 1)
