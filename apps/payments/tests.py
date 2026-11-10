"""Payments are external declarations, not receipts issued by ConecTA."""
from datetime import timedelta
from decimal import Decimal

from django.contrib.auth import get_user_model
from django.utils import timezone
from rest_framework.test import APITestCase

from apps.accounts.models import Employer, Worker
from apps.contracts.models import AgreementApproval, AgreementVersion, Contract
from apps.contracts.services import (
    approve_version, open_amendment, save_draft, submit_draft,
)
from apps.marketplace.models import Offer, Proposal

from .models import ExternalPayment, ExternalPaymentEvent

User = get_user_model()
PASSWORD = "Demo-Secure_2026!"


class ExternalPaymentTests(APITestCase):
    def setUp(self):
        self.employer = User.objects.create_user(
            username="owner", name="Empregador Exemplo",
            email="owner@example.test", phone="+258841000001", password=PASSWORD
        )
        self.worker = User.objects.create_user(
            username="worker", name="Trabalhador Exemplo",
            email="worker@example.test", phone="+258841000002", password=PASSWORD
        )
        self.outsider = User.objects.create_user(
            username="outsider", name="Terceiro Exemplo",
            email="outsider@example.test", phone="+258841000003", password=PASSWORD
        )
        self.ep = Employer.objects.create(
            user=self.employer, company_name="Empresa Teste", address="Maputo"
        )
        self.wp = Worker.objects.create(
            user=self.worker, skills="Python", experience="3 anos"
        )
        offer = Offer.objects.create(
            employer=self.ep, title="Portal informático",
            description="Portal de demonstração para oportunidades de TI em Maputo.",
            category="Desenvolvimento Web", required_skills=["Python"],
            budget=Decimal("20000.00"), location="Maputo",
        )
        proposal = Proposal.objects.create(
            offer=offer, worker=self.wp, description="Entrega em duas etapas.",
            proposed_amount=Decimal("20000.00"), timeline_days=20,
        )
        self.contract = Contract.objects.create(
            offer=offer, proposal=proposal, employer=self.ep, worker=self.wp,
            title=offer.title, scope=offer.description, budget=Decimal("20000.00"),
            status=Contract.Status.ACTIVE,
        )
        self.terms = {
            "title": "Portal de serviços técnicos",
            "scope": "Desenvolver portal web para serviços e oportunidades de TI.",
            "deliverables": "Código-fonte, testes de integração e documentação técnica.",
            "acceptance_criteria": "Fluxos de propostas, mensagens e procura aprovados.",
            "budget": "20000.00", "start_date": "2026-11-10",
            "end_date": "2026-12-20",
            "payment_conditions": [
                {
                    "id": "advance", "stage": "ADVANCE", "method": "M-Pesa",
                    "amount": "4000.00", "moment": "Após aprovação bilateral do acordo",
                },
                {
                    "id": "final", "stage": "FINAL", "method": "e-Mola",
                    "amount": "16000.00", "moment": "Depois da aceitação da entrega final",
                },
            ],
        }
        self.agreement = AgreementVersion.objects.create(
            contract=self.contract, created_by=self.employer,
            number=1, status=AgreementVersion.Status.ACTIVE,
            terms=self.terms, reason="Contrato sintético aceite por ambas as partes.",
        )
        AgreementApproval.objects.create(
            version=self.agreement, user=self.employer, party="employer"
        )
        AgreementApproval.objects.create(
            version=self.agreement, user=self.worker, party="worker"
        )
        self.url = f"/api/payments/contracts/{self.contract.id}/"
        self.payload = {
            "amount": "3000.00", "method": "M-Pesa", "stage": "ADVANCE",
            "moment": "Após aprovação bilateral do acordo",
            "agreement_condition_id": "advance",
            "paid_on": timezone.localdate().isoformat(),
            "external_reference": "REF-DEMONSTRACAO-001",
        }

    def report(self, payload=None):
        self.client.force_authenticate(user=self.employer)
        response = self.client.post(self.url, payload or self.payload, format="json")
        self.assertEqual(response.status_code, 201, response.data)
        return response

    def test_only_employer_can_report_external_payment(self):
        for actor, expected in [(None, 401), (self.worker, 403), (self.outsider, 403)]:
            self.client.force_authenticate(user=actor)
            response = self.client.post(self.url, self.payload, format="json")
            self.assertEqual(response.status_code, expected)
        self.assertEqual(ExternalPayment.objects.count(), 0)
        self.report()
        self.assertEqual(ExternalPayment.objects.count(), 1)

    def test_report_is_not_a_transfer_and_retains_source_version(self):
        response = self.report()
        self.assertEqual(response.data["status"], "REPORTED_PAID")
        self.assertEqual(response.data["agreement_version_id"], self.agreement.id)
        self.assertEqual(response.data["agreement_condition_id"], "advance")
        self.assertEqual(response.data["reported_by_user_id"], self.employer.id)
        self.assertEqual(len(response.data["history"]), 1)
        self.assertIn("não verificou", response.data["history"][0]["note"])
        self.contract.refresh_from_db()
        self.assertEqual(self.contract.status, Contract.Status.ACTIVE)

    def test_payments_are_private_to_both_parties(self):
        self.report()
        self.client.force_authenticate(user=self.outsider)
        self.assertEqual(self.client.get(self.url).status_code, 403)
        self.client.force_authenticate(user=None)
        self.assertEqual(self.client.get(self.url).status_code, 401)
        self.client.force_authenticate(user=self.worker)
        items = self.client.get(self.url)
        self.assertEqual(items.status_code, 200)
        self.assertEqual(len(items.data), 1)

    def test_wrong_stage_method_or_condition_is_rejected(self):
        for changed in [
            {"method": "e-Mola"},
            {"stage": "FINAL"},
            {"agreement_condition_id": "unknown"},
            {"moment": "Momento não acordado"},
        ]:
            self.client.force_authenticate(user=self.employer)
            r = self.client.post(self.url, {**self.payload, **changed}, format="json")
            self.assertEqual(r.status_code, 400, r.data)
        self.assertEqual(ExternalPayment.objects.count(), 0)

    def test_invalid_amount_and_future_date_are_rejected(self):
        for changed in [
            {"amount": "0.00"},
            {"amount": "-1.00"},
            {"amount": "3000.001"},
            {"paid_on": (timezone.localdate() + timedelta(days=1)).isoformat()},
        ]:
            self.client.force_authenticate(user=self.employer)
            r = self.client.post(self.url, {**self.payload, **changed}, format="json")
            self.assertEqual(r.status_code, 400, r.data)
        self.assertEqual(ExternalPayment.objects.count(), 0)

    def test_sum_cannot_exceed_approved_milestone(self):
        self.report()
        self.client.force_authenticate(user=self.employer)
        r = self.client.post(self.url, {
            **self.payload, "amount": "1000.01",
        }, format="json")
        self.assertEqual(r.status_code, 400)
        self.assertEqual(ExternalPayment.objects.count(), 1)

    def test_worker_confirms_once_with_audit_trail(self):
        record = self.report().data
        self.client.force_authenticate(user=self.worker)
        url = f"/api/payments/{record['id']}/respond/"
        confirmed = self.client.post(url, {"action": "CONFIRMED"}, format="json")
        self.assertEqual(confirmed.status_code, 200, confirmed.data)
        self.assertEqual(confirmed.data["status"], "CONFIRMED")
        self.assertEqual(confirmed.data["responded_by_user_id"], self.worker.id)
        self.assertEqual(len(confirmed.data["history"]), 2)
        self.assertEqual(self.client.post(url, {"action": "CONTESTED", "reason": "Atraso de confirmação"}, format="json").status_code, 409)
        self.assertEqual(ExternalPaymentEvent.objects.count(), 2)

    def test_contestation_requires_reason_and_has_no_banking_effect(self):
        record = self.report().data
        self.client.force_authenticate(user=self.worker)
        url = f"/api/payments/{record['id']}/respond/"
        self.assertEqual(self.client.post(url, {
            "action": "CONTESTED", "reason": "curto"
        }, format="json").status_code, 400)
        result = self.client.post(url, {
            "action": "CONTESTED", "reason": "Este valor não foi recebido na conta indicada."
        }, format="json")
        self.assertEqual(result.status_code, 200, result.data)
        self.assertEqual(result.data["status"], "CONTESTED")
        self.contract.refresh_from_db()
        self.assertEqual(self.contract.status, Contract.Status.ACTIVE)

    def test_employer_and_third_party_cannot_confirm(self):
        record = self.report().data
        url = f"/api/payments/{record['id']}/respond/"
        for actor, status_code in [(self.employer, 403), (self.outsider, 403)]:
            self.client.force_authenticate(user=actor)
            self.assertEqual(self.client.post(url, {"action": "CONFIRMED"}, format="json").status_code, status_code)
        self.assertEqual(ExternalPayment.objects.get(id=record["id"]).status, "REPORTED_PAID")

    def test_unapproved_contract_cannot_receive_declarations(self):
        self.contract.status = Contract.Status.PENDING
        self.contract.save(update_fields=["status"])
        self.client.force_authenticate(user=self.employer)
        self.assertEqual(self.client.post(self.url, self.payload, format="json").status_code, 409)
        self.assertEqual(ExternalPayment.objects.count(), 0)

    def test_amendment_cannot_reduce_budget_below_declared_amount(self):
        self.report()
        version = open_amendment(
            self.contract.id, self.employer,
            "Nova versão com orçamento artificialmente inferior ao pago"
        )
        amended = dict(self.terms)
        amended["budget"] = "2000.00"
        amended["payment_conditions"] = [
            {**self.terms["payment_conditions"][0], "amount": "2000.00"}
        ]
        save_draft(version.id, self.employer, amended)
        submit_draft(version.id, self.employer)
        approve_version(version.id, self.employer)
        from apps.contracts.services import Conflict
        with self.assertRaises(Conflict):
            approve_version(version.id, self.worker)
        version.refresh_from_db()
        self.assertEqual(version.approvals.count(), 1)
        self.contract.refresh_from_db()
        self.assertEqual(self.contract.budget, Decimal("20000.00"))

    def test_only_one_active_version_accepted_for_declarations(self):
        self.report()
        self.agreement.status = AgreementVersion.Status.SUPERSEDED
        self.agreement.save(update_fields=["status"])
        self.client.force_authenticate(user=self.employer)
        r = self.client.post(self.url, self.payload, format="json")
        self.assertEqual(r.status_code, 409)
