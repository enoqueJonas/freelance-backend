"""RN13/RN14/RN16: non-arbitral documentary dispute tracking."""
from decimal import Decimal

from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase

from apps.accounts.models import Employer, Worker
from apps.contracts.models import Contract, Dispute, DisputeEvidence, DisputeEvent
from apps.marketplace.models import Offer, Proposal

User = get_user_model()


class DisputeApiTests(APITestCase):
    def setUp(self):
        self.employer = User.objects.create_user(
            username="employer", name="Empregador Demo",
            email="employer@example.test", phone="+258841000001", password="Strong-Example_987!"
        )
        self.worker = User.objects.create_user(
            username="worker", name="Trabalhador Demo",
            email="worker@example.test", phone="+258841000002", password="Strong-Example_987!"
        )
        self.admin = User.objects.create_user(
            username="admin", name="Moderador Demo", email="admin@example.test",
            phone="+258841000003", password="Strong-Example_987!", is_staff=True
        )
        self.outsider = User.objects.create_user(
            username="outside", name="Terceiro", email="outsider@example.test",
            phone="+258841000004", password="Strong-Example_987!"
        )
        ep = Employer.objects.create(
            user=self.employer, company_name="Empresa Demo", address="Maputo"
        )
        wp = Worker.objects.create(
            user=self.worker, skills="Python", experience="2 anos"
        )
        offer = Offer.objects.create(
            employer=ep, title="Sistema de serviços TI",
            description="Criar um portal para trabalhadores e empregadores na cidade de Maputo.",
            category="Desenvolvimento Web", required_skills=["Python"],
            budget=Decimal("16000.00"), location="Maputo",
        )
        proposal = Proposal.objects.create(
            offer=offer, worker=wp,
            description="Desenvolvimento web com documentação.", proposed_amount=Decimal("15000.00"),
            timeline_days=20,
        )
        self.contract = Contract.objects.create(
            offer=offer, proposal=proposal, worker=wp, employer=ep,
            title=offer.title, scope=offer.description, budget=Decimal("15000.00"),
            status=Contract.Status.ACTIVE,
        )
        self.url = "/api/disputes/"
        self.report_payload = {
            "contract_id": self.contract.id,
            "category": "DELIVERABLE",
            "description": "O relatório de testes acordado não foi entregue até à data prevista.",
            "evidence_description": "Registo descritivo de exemplo da lista de entregáveis.",
            "evidence_url": "https://example.test/documentacao-sintetica",
        }

    def report(self, actor=None):
        self.client.force_authenticate(user=actor or self.worker)
        res = self.client.post(self.url, self.report_payload, format="json")
        self.assertEqual(res.status_code, 201, res.data)
        return res

    def administrative(self, case_id, action, data=None, actor=None):
        self.client.force_authenticate(user=actor or self.admin)
        return self.client.post(
            f"/api/disputes/{case_id}/{action}/", data or {}, format="json"
        )

    def test_worker_report_creates_descriptive_evidence_and_open_event(self):
        d = self.report().data
        self.assertEqual(d["status"], "OPEN")
        self.assertEqual(d["category"], "DELIVERABLE")
        self.assertEqual(d["reported_by_user_id"], self.worker.id)
        self.assertEqual(d["contract_id"], self.contract.id)
        self.assertEqual(len(d["evidence"]), 1)
        self.assertEqual(d["evidence"][0]["author_user_id"], self.worker.id)
        self.assertEqual(d["events"][0]["action"], "REPORTED")
        self.contract.refresh_from_db()
        self.assertEqual(self.contract.status, Contract.Status.ACTIVE)

    def test_employer_may_report_but_admin_and_outsider_cannot_report_for_parties(self):
        d = self.report(self.employer).data
        self.assertEqual(d["reported_by_user_id"], self.employer.id)
        for actor in (self.admin, self.outsider):
            self.client.force_authenticate(user=actor)
            res = self.client.post(self.url, self.report_payload, format="json")
            self.assertEqual(res.status_code, 403)
        self.assertEqual(Dispute.objects.count(), 1)

    def test_private_dispute_visibility_and_admin_read_only_directory(self):
        d = self.report().data
        self.client.force_authenticate(user=self.outsider)
        self.assertEqual(self.client.get(self.url).data, [])
        self.assertEqual(self.client.get(f"/api/disputes/{d['id']}/").status_code, 404)
        self.client.force_authenticate(user=None)
        self.assertEqual(self.client.get(self.url).status_code, 401)
        for actor in (self.employer, self.worker, self.admin):
            self.client.force_authenticate(user=actor)
            self.assertEqual(len(self.client.get(self.url).data), 1)
            self.assertEqual(self.client.get(f"/api/disputes/{d['id']}/").status_code, 200)

    def test_invalid_category_short_description_or_unsafe_evidence_url(self):
        variants = [
            {"category": "ARBITRATION"},
            {"description": "curta"},
            {"evidence_description": "pouco"},
            {"evidence_url": "javascript:alert(1)"},
            {"evidence_url": "ftp://example.test/a"},
        ]
        self.client.force_authenticate(user=self.worker)
        for changes in variants:
            r = self.client.post(
                self.url, {**self.report_payload, **changes}, format="json"
            )
            self.assertEqual(r.status_code, 400, r.data)
        self.assertEqual(Dispute.objects.count(), 0)

    def test_only_staff_can_start_review_and_must_start_at_open(self):
        d = self.report().data
        r = self.administrative(d["id"], "begin-review", {
            "note": "Revisão da evidência de demonstração"
        }, actor=self.worker)
        self.assertEqual(r.status_code, 403)
        r = self.administrative(d["id"], "begin-review", {"note": "curto"})
        self.assertEqual(r.status_code, 400)
        r = self.administrative(d["id"], "begin-review", {
            "note": "Analisar relatos descritivos do contrato"
        })
        self.assertEqual(r.status_code, 200, r.data)
        self.assertEqual(r.data["status"], "UNDER_REVIEW")
        self.assertEqual(r.data["events"][-1]["action"], "REVIEW_STARTED")
        self.assertEqual(self.administrative(
            d["id"], "begin-review", {"note": "Iniciar de novo a análise"}
        ).status_code, 409)

    def test_request_information_targets_only_a_contracting_party(self):
        d = self.report().data
        self.administrative(d["id"], "begin-review", {
            "note": "Iniciar análise administrativa"
        })
        bad = self.administrative(d["id"], "request-information", {
            "requested_from_user_id": self.outsider.id,
            "note": "Solicitar documentos de suporte"
        })
        self.assertEqual(bad.status_code, 403)
        requested = self.administrative(d["id"], "request-information", {
            "requested_from_user_id": self.worker.id,
            "note": "Disponibilize a lista dos entregáveis aprovados."
        })
        self.assertEqual(requested.status_code, 200, requested.data)
        self.assertEqual(requested.data["status"], "WAITING_INFORMATION")
        self.assertEqual(requested.data["requested_from_user_id"], self.worker.id)
        self.assertEqual(requested.data["events"][-1]["action"], "INFORMATION_REQUESTED")

    def test_information_by_other_party_does_not_satisfy_directed_request(self):
        d = self.report().data
        self.administrative(d["id"], "begin-review", {
            "note": "Começar a análise documental"
        })
        self.administrative(d["id"], "request-information", {
            "requested_from_user_id": self.worker.id,
            "note": "Solicita-se documentação adicional."
        })
        self.client.force_authenticate(user=self.employer)
        response = self.client.post(f"/api/disputes/{d['id']}/evidence/", {
            "description": "Documentação complementar adicionada pelo empregador."
        })
        self.assertEqual(response.status_code, 200, response.data)
        self.assertEqual(response.data["status"], "WAITING_INFORMATION")
        self.assertEqual(response.data["requested_from_user_id"], self.worker.id)
        self.assertEqual(response.data["events"][-1]["action"], "EVIDENCE_ADDED")

    def test_requested_party_answer_returns_to_review_with_actor_and_date(self):
        d = self.report().data
        self.administrative(d["id"], "begin-review", {
            "note": "Conferência de ocorrência"
        })
        self.administrative(d["id"], "request-information", {
            "requested_from_user_id": self.worker.id,
            "note": "Recolha evidência complementar do pedido."
        })
        self.client.force_authenticate(user=self.worker)
        r = self.client.post(f"/api/disputes/{d['id']}/evidence/", {
            "description": "Histórico descritivo e referência de mensagem de teste."
        })
        self.assertEqual(r.status_code, 200, r.data)
        self.assertEqual(r.data["status"], "UNDER_REVIEW")
        self.assertIsNone(r.data["requested_from_user_id"])
        self.assertEqual(r.data["events"][-1]["action"], "INFORMATION_SUPPLIED")
        self.assertEqual(r.data["events"][-1]["actor_user_id"], self.worker.id)
        self.assertTrue(r.data["events"][-1]["recorded_at"])

    def test_admin_result_and_closure_are_not_contract_arbitration(self):
        d = self.report().data
        self.administrative(d["id"], "begin-review", {
            "note": "Analisar informação recebida"
        })
        concluded = self.administrative(d["id"], "result", {
            "note": "Foram organizadas as evidências e comunicadas às partes; não houve decisão vinculativa."
        })
        self.assertEqual(concluded.status_code, 200, concluded.data)
        self.assertEqual(concluded.data["status"], "RESOLVED")
        self.assertIn("não houve", concluded.data["administrative_result"])
        closed = self.administrative(d["id"], "close", {
            "note": "Acompanhamento documental concluído."
        })
        self.assertEqual(closed.status_code, 200, closed.data)
        self.assertEqual(closed.data["status"], "CLOSED")
        self.contract.refresh_from_db()
        self.assertEqual(self.contract.status, Contract.Status.ACTIVE)
        self.assertEqual(DisputeEvent.objects.filter(dispute_id=d["id"]).count(), 4)

    def test_invalid_administrative_transitions_have_no_mutation(self):
        d = self.report().data
        self.assertEqual(self.administrative(d["id"], "result", {
            "note": "Não deve existir resultado sem análise administrativa."
        }).status_code, 409)
        self.assertEqual(self.administrative(d["id"], "close", {
            "note": "Tentativa de encerramento prematuro"
        }).status_code, 409)
        self.assertEqual(self.administrative(d["id"], "request-information", {
            "requested_from_user_id": self.worker.id,
            "note": "Pedido inválido fora de análise"
        }).status_code, 409)
        self.assertEqual(Dispute.objects.get(id=d["id"]).status, "OPEN")
        self.assertEqual(DisputeEvent.objects.filter(dispute_id=d["id"]).count(), 1)

    def test_closed_or_resolved_case_cannot_receive_more_evidence(self):
        d = self.report().data
        self.administrative(d["id"], "begin-review", {
            "note": "Iniciar análise documental"
        })
        self.administrative(d["id"], "result", {
            "note": "O acompanhamento foi documentado e comunicado sem arbitragem."
        })
        self.client.force_authenticate(user=self.worker)
        self.assertEqual(self.client.post(
            f"/api/disputes/{d['id']}/evidence/",
            {"description": "Tentativa de acrescentar evidência após conclusão."}
        ).status_code, 409)
        self.administrative(d["id"], "close", {
            "note": "Encerrar acompanhamento documentado."
        })
        self.client.force_authenticate(user=self.employer)
        self.assertEqual(self.client.post(
            f"/api/disputes/{d['id']}/evidence/",
            {"description": "Informação enviada após encerramento."}
        ).status_code, 409)
        self.assertEqual(DisputeEvidence.objects.filter(dispute_id=d["id"]).count(), 1)

    def test_admin_cannot_submit_party_evidence_and_outsider_cannot_see_it(self):
        d = self.report().data
        self.client.force_authenticate(user=self.admin)
        self.assertEqual(self.client.post(
            f"/api/disputes/{d['id']}/evidence/",
            {"description": "Admin não pode criar evidência como uma parte."}
        ).status_code, 403)
        self.client.force_authenticate(user=self.outsider)
        self.assertEqual(self.client.post(
            f"/api/disputes/{d['id']}/evidence/",
            {"description": "Terceiro sem permissão de acesso."}
        ).status_code, 404)
