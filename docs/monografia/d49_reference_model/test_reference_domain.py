"""Ensaios EXCLUSIVOS do modelo de referência D49. Não testam Django nem React."""
import unittest
from reference_domain import (
    Engagement, RuleError, EngagementStatus as ES,
    AgreementStatus as AS, DisputeStatus as DS, PaymentStatus as PS,
)


def active():
    e = Engagement(worker=101, employer=202, admin_ids=frozenset({999}))
    v = e.propose(101, 'Entregar website por 10 000 MZN')
    e.accept(101, v.number, v.digest)
    e.accept(202, v.number, v.digest)
    return e


class AcceptanceModelTests(unittest.TestCase):
    def assertRejects(self, action):
        with self.assertRaises(RuleError):
            action()

    def test_G01_auto_contratacao_bloqueada(self):
        self.assertRejects(lambda: Engagement(worker=7, employer=7))

    def test_G02_criacao_pendente_sem_versao(self):
        e = Engagement(101, 202)
        self.assertEqual(e.status, ES.PENDING_AGREEMENT)
        self.assertEqual(len(e.versions), 0)

    def test_G03_duas_aceitacoes_obrigatorias(self):
        e = Engagement(101, 202)
        v = e.propose(101, 'Acordo v1')
        e.accept(101, 1, v.digest)
        self.assertEqual(e.status, ES.PENDING_AGREEMENT)
        e.accept(202, 1, v.digest)
        self.assertEqual(e.status, ES.ACTIVE)
        self.assertEqual(e.versions[v.number - 1].status, AS.ACCEPTED)

    def test_G03_actor_estranho_nao_aceita(self):
        e = Engagement(101, 202)
        v = e.propose(101, 'Acordo v1')
        self.assertRejects(lambda: e.accept(303, 1, v.digest))

    def test_G03_aceitacao_duplicada_bloqueada(self):
        e = Engagement(101, 202)
        v = e.propose(101, 'Acordo v1')
        e.accept(101, 1, v.digest)
        self.assertRejects(lambda: e.accept(101, 1, v.digest))

    def test_G04_rejeitar_v2_preserva_v1(self):
        e = active()
        old = e.versions[0]
        v2 = e.propose(202, 'Novo prazo e preco')
        e.reject(101, v2.number)
        self.assertEqual(old.status, AS.ACCEPTED)
        self.assertEqual(old.terms, 'Entregar website por 10 000 MZN')
        self.assertEqual(e.versions[1].status, AS.REJECTED)
        self.assertEqual(e.status, ES.ACTIVE)

    def test_G04_aceitar_v2_preserva_historico(self):
        e = active()
        v2 = e.propose(202, 'Prazo de 14 dias')
        e.accept(101, 2, v2.digest)
        e.accept(202, 2, v2.digest)
        self.assertEqual([v.number for v in e.versions], [1, 2])
        self.assertEqual(e.versions[0].status, AS.ACCEPTED)
        self.assertEqual(e.versions[1].status, AS.ACCEPTED)

    def test_G05_nao_concluir_sem_entrega(self):
        e = active()
        self.assertRejects(lambda: e.complete(202))
        self.assertEqual(e.status, ES.ACTIVE)

    def test_G06_entrega_e_conclusao_por_actores_correctos(self):
        e = active()
        self.assertRejects(lambda: e.deliver(202))
        e.deliver(101)
        self.assertEqual(e.status, ES.DELIVERED)
        self.assertRejects(lambda: e.complete(101))
        e.complete(202)
        self.assertEqual(e.status, ES.COMPLETED)

    def test_G07_conflito_nao_apaga_estado_do_servico(self):
        e = active()
        e.deliver(101)
        d = e.open_dispute(202)
        self.assertEqual(d.status, DS.OPEN)
        self.assertEqual(e.status, ES.DELIVERED)

    def test_G08_encerramento_do_conflito_nao_conclui_servico(self):
        e = active()
        d = e.open_dispute(101)
        for status in (DS.UNDER_REVIEW, DS.WAITING_INFORMATION, DS.UNDER_REVIEW, DS.RESOLVED, DS.CLOSED):
            e.dispute_transition(999, d.number, status)
        self.assertEqual(e.status, ES.ACTIVE)
        self.assertEqual(d.status, DS.CLOSED)

    def test_G09_reportar_pagamento_nao_equivale_a_confirmar(self):
        e = active()
        p = e.report_payment(202, 5000)
        self.assertEqual(p.status, PS.REPORTED_PAID)

    def test_G10_pagador_nao_autoconfirma_pagamento(self):
        e = active()
        p = e.report_payment(202, 5000)
        self.assertRejects(lambda: e.payment_transition(202, p.number, PS.CONFIRMED))
        self.assertEqual(p.status, PS.REPORTED_PAID)

    def test_G10_recebedor_pode_confirmar_pagamento_manual(self):
        e = active()
        p = e.report_payment(202, 5000)
        e.payment_transition(101, p.number, PS.CONFIRMED)
        self.assertEqual(p.status, PS.CONFIRMED)

    def test_G11_contestacao_financeira_nao_muda_entrega(self):
        e = active()
        e.deliver(101)
        p = e.report_payment(202, 5000)
        e.payment_transition(101, p.number, PS.DISPUTED)
        self.assertEqual(e.status, ES.DELIVERED)
        self.assertEqual(p.status, PS.DISPUTED)

    def test_G12_eventos_tem_identificador_actor_e_accao(self):
        e = active()
        e.deliver(101)
        self.assertEqual([v[0] for v in e.events], list(range(1, len(e.events) + 1)))
        self.assertTrue(all(v[1] and v[2] and v[3].endswith("+00:00") for v in e.events))

    def test_G13_actor_estranho_sem_direito_sobre_acordo(self):
        e = active()
        self.assertRejects(lambda: e.propose(303, 'intrusao'))

    def test_G13_so_admin_pode_encaminhar_disputa(self):
        e = active()
        d = e.open_dispute(101)
        self.assertRejects(lambda: e.dispute_transition(202, d.number, DS.UNDER_REVIEW))

    def test_G14_admin_nao_tem_poder_de_concluir_contrato(self):
        e = active()
        d = e.open_dispute(101)
        e.dispute_transition(999, d.number, DS.UNDER_REVIEW)
        e.dispute_transition(999, d.number, DS.RESOLVED)
        self.assertEqual(e.status, ES.ACTIVE)

    def test_G15_nao_ha_integracao_psp_no_modelo_de_referencia(self):
        e = active()
        self.assertFalse(hasattr(e, 'charge_card'))
        self.assertFalse(hasattr(e, 'transfer_funds'))

    def test_G16_versao_com_conteudo_diferente_rejeitada(self):
        e = Engagement(101, 202)
        v = e.propose(101, 'Condicoes originais')
        self.assertRejects(lambda: e.accept(202, 1, 'outro-hash'))
        self.assertEqual(e.versions[v.number - 1].status, AS.PROPOSED)

    def test_guard_nao_se_pode_propor_segunda_versao_pendente(self):
        e = Engagement(101, 202)
        e.propose(101, 'v1')
        self.assertRejects(lambda: e.propose(202, 'v2'))

    def test_guard_versao_aceite_e_imutavel(self):
        from dataclasses import FrozenInstanceError
        e = active()
        with self.assertRaises(FrozenInstanceError):
            e.versions[0].terms = 'alterado'
        self.assertEqual(e.current_accepted_version.number, 1)

    def test_guard_revisao_preserva_historico(self):
        e = active()
        e.deliver(101)
        e.request_revision(202)
        self.assertEqual(e.status, ES.ACTIVE)
        self.assertEqual(e.delivery_records, 1)

    def test_guard_revisao_por_estranho_rejeitada(self):
        e = active()
        e.deliver(101)
        self.assertRejects(lambda: e.request_revision(303))

    def test_guard_versao_nao_pode_ser_aceite_apos_cancelamento(self):
        e = Engagement(101, 202)
        v = e.propose(101, 'Termos a aprovar')
        e.accept(101, v.number, v.digest)
        e.cancel(202, permitted_by_policy=True)
        self.assertRejects(lambda: e.accept(202, v.number, v.digest))
        self.assertEqual(e.status, ES.CANCELLED)

    def test_guard_pagamento_sem_acordo_aceite_proibido(self):
        e = Engagement(101, 202)
        self.assertRejects(lambda: e.report_payment(202, 4000))

    def test_guard_identidade_das_partes_imutavel(self):
        e = Engagement(101, 202)
        self.assertRejects(lambda: setattr(e, 'worker', 202))

    def test_guard_identificadores_invalidos_rejeitados(self):
        e = active()
        self.assertRejects(lambda: e.accept(101, 99, 'hash'))
        self.assertRejects(lambda: e.reject(101, 99))
        self.assertRejects(lambda: e.payment_transition(101, 99, PS.CONFIRMED))
        self.assertRejects(lambda: e.dispute_transition(999, 99, DS.UNDER_REVIEW))

    def test_guard_dupla_confirmacao_pagamento_rejeitada(self):
        e = active()
        p = e.report_payment(202, 1000)
        e.payment_transition(101, p.number, PS.CONFIRMED)
        self.assertRejects(lambda: e.payment_transition(101, p.number, PS.CONFIRMED))

    def test_guard_cancelamento_exige_politica(self):
        e = Engagement(101, 202)
        self.assertRejects(lambda: e.cancel(101))
        e.cancel(101, permitted_by_policy=True)
        self.assertEqual(e.status, ES.CANCELLED)

    def test_guard_transicao_de_disputa_ilegal_bloqueada(self):
        e = active()
        d = e.open_dispute(101)
        self.assertRejects(lambda: e.dispute_transition(999, d.number, DS.CLOSED))


if __name__ == '__main__':
    unittest.main()