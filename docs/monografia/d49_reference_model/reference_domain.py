"""D49: MODELO DE REFERÊNCIA para testar invariantes do desenho ConecTA.

Não é o backend Django, não autentica utilizadores e não comprova testes do protótipo.
Decisões propostas: B (ciclos separados), B1 (0..* versões), aceites explícitos.
"""
from dataclasses import dataclass, field, replace
from datetime import datetime, timezone
from enum import Enum
import hashlib


class RuleError(ValueError):
    pass


class EngagementStatus(str, Enum):
    PENDING_AGREEMENT = 'PENDING_AGREEMENT'
    ACTIVE = 'ACTIVE'
    DELIVERED = 'DELIVERED'
    COMPLETED = 'COMPLETED'
    CANCELLED = 'CANCELLED'


class AgreementStatus(str, Enum):
    PROPOSED = 'PROPOSED'
    ACCEPTED = 'ACCEPTED'
    REJECTED = 'REJECTED'


class DisputeStatus(str, Enum):
    OPEN = 'OPEN'
    UNDER_REVIEW = 'UNDER_REVIEW'
    WAITING_INFORMATION = 'WAITING_INFORMATION'
    RESOLVED = 'RESOLVED'
    CLOSED = 'CLOSED'


class PaymentStatus(str, Enum):
    REPORTED_PAID = 'REPORTED_PAID'
    CONFIRMED = 'CONFIRMED'
    DISPUTED = 'DISPUTED'


@dataclass(frozen=True)
class AgreementVersion:
    number: int
    terms: str
    digest: str
    status: AgreementStatus = AgreementStatus.PROPOSED
    approvals: frozenset[int] = frozenset()


@dataclass
class DisputeCase:
    number: int
    status: DisputeStatus = DisputeStatus.OPEN


@dataclass
class PaymentRecord:
    number: int
    value: int
    status: PaymentStatus = PaymentStatus.REPORTED_PAID


@dataclass
class Engagement:
    worker: int
    employer: int
    status: EngagementStatus = EngagementStatus.PENDING_AGREEMENT
    versions: list[AgreementVersion] = field(default_factory=list)
    disputes: list[DisputeCase] = field(default_factory=list)
    payments: list[PaymentRecord] = field(default_factory=list)
    events: list[tuple[int, str, str, str]] = field(default_factory=list)
    admin_ids: frozenset[int] = frozenset()
    delivery_records: int = 0
    next_event: int = 1

    def __post_init__(self):
        if self.worker == self.employer:
            raise RuleError('G01: não se pode contratar a si mesmo')
        self._event(self.employer, 'PROPOSAL_ACCEPTED')

    def _event(self, actor: int, action: str):
        self.events.append((self.next_event, str(actor), action, datetime.now(timezone.utc).isoformat()))
        self.next_event += 1

    def _party(self, actor: int):
        if actor not in (self.worker, self.employer):
            raise RuleError('G13: apenas parte da contratação')

    def _accepted(self):
        return [v for v in self.versions if v.status is AgreementStatus.ACCEPTED]

    def propose(self, actor: int, terms: str) -> AgreementVersion:
        self._party(actor)
        if self.status not in (EngagementStatus.PENDING_AGREEMENT, EngagementStatus.ACTIVE):
            raise RuleError('acordo não editável neste estado')
        if not terms.strip():
            raise RuleError('termos vazios')
        if any(v.status is AgreementStatus.PROPOSED for v in self.versions):
            raise RuleError('já existe uma proposta pendente')
        version = AgreementVersion(len(self.versions) + 1, terms, hashlib.sha256(terms.encode()).hexdigest())
        self.versions.append(version)
        self._event(actor, f'AGREEMENT_V{version.number}_PROPOSED')
        return version

    def accept(self, actor: int, number: int, digest: str):
        self._party(actor)
        if number < 1 or number > len(self.versions):
            raise RuleError("versão inexistente")
        v = self.versions[number - 1]
        if v.status is not AgreementStatus.PROPOSED or v.digest != digest:
            raise RuleError('G03/G16: versão inválida, rejeitada ou conteúdo divergente')
        if actor in v.approvals:
            raise RuleError('aceitação duplicada')
        approvals = v.approvals | {actor}
        self.versions[number - 1] = replace(v, approvals=approvals,
            status=(AgreementStatus.ACCEPTED if approvals == {self.worker, self.employer} else AgreementStatus.PROPOSED))
        self._event(actor, f'AGREEMENT_V{v.number}_APPROVED')
        if approvals == {self.worker, self.employer}:
            # Versão aceite anterior continua preservada e não é alterada.
            if self.status is EngagementStatus.PENDING_AGREEMENT:
                self.status = EngagementStatus.ACTIVE
            self._event(actor, f'AGREEMENT_V{v.number}_ACCEPTED')

    def reject(self, actor: int, number: int):
        self._party(actor)
        v = self.versions[number - 1]
        if v.status is not AgreementStatus.PROPOSED:
            raise RuleError('só propostas pendentes podem ser rejeitadas')
        self.versions[number - 1] = replace(v, status=AgreementStatus.REJECTED)
        self._event(actor, f'AGREEMENT_V{v.number}_REJECTED')

    @property
    def current_accepted_version(self) -> AgreementVersion | None:
        return next((v for v in reversed(self.versions) if v.status is AgreementStatus.ACCEPTED), None)

    def request_revision(self, actor: int):
        if actor != self.employer or self.status is not EngagementStatus.DELIVERED:
            raise RuleError("revisão exige solicitação da parte contratante após entrega")
        self.status = EngagementStatus.ACTIVE
        self._event(actor, "REVISION_REQUESTED")

    def deliver(self, actor: int):
        if actor != self.worker or self.status is not EngagementStatus.ACTIVE or not self._accepted():
            raise RuleError('G05: entrega exige trabalhador e acordo aceite activo')
        self.delivery_records += 1
        self.status = EngagementStatus.DELIVERED
        self._event(actor, 'DELIVERED')

    def complete(self, actor: int):
        if actor != self.employer or self.status is not EngagementStatus.DELIVERED or self.delivery_records < 1:
            raise RuleError('G05/G06: conclusão exige entrega e confirmação do empregador')
        self.status = EngagementStatus.COMPLETED
        self._event(actor, 'COMPLETED')

    def open_dispute(self, actor: int) -> DisputeCase:
        self._party(actor)
        if self.status not in (EngagementStatus.ACTIVE, EngagementStatus.DELIVERED):
            raise RuleError('estados permitidos para reportar conflito ainda sujeitos a decisão')
        d = DisputeCase(len(self.disputes) + 1)
        self.disputes.append(d)
        self._event(actor, f'DISPUTE_{d.number}_OPEN')
        return d

    def dispute_transition(self, admin: int, number: int, target: DisputeStatus):
        if admin not in self.admin_ids:
            raise RuleError('G13: acto administrativo não autorizado')
        d = self.disputes[number - 1]
        valid = {
            DisputeStatus.OPEN: {DisputeStatus.UNDER_REVIEW},
            DisputeStatus.UNDER_REVIEW: {DisputeStatus.WAITING_INFORMATION, DisputeStatus.RESOLVED},
            DisputeStatus.WAITING_INFORMATION: {DisputeStatus.UNDER_REVIEW},
            DisputeStatus.RESOLVED: {DisputeStatus.CLOSED},
            DisputeStatus.CLOSED: set(),
        }
        if target not in valid[d.status]:
            raise RuleError('transição administrativa inválida')
        d.status = target
        self._event(admin, f'DISPUTE_{number}_{target.value}')

    def report_payment(self, actor: int, value: int) -> PaymentRecord:
        if actor != self.employer or value <= 0 or self.status is EngagementStatus.CANCELLED:
            raise RuleError('G09: só pagador pode reportar um valor positivo')
        payment = PaymentRecord(len(self.payments) + 1, value)
        self.payments.append(payment)
        self._event(actor, f'PAYMENT_{payment.number}_REPORTED_PAID')
        return payment

    def payment_transition(self, actor: int, number: int, target: PaymentStatus):
        # Política candidata: contraparte recebedora pode confirmar/contestar registo manual.
        if actor != self.worker or target not in (PaymentStatus.CONFIRMED, PaymentStatus.DISPUTED):
            raise RuleError('G10: confirmação/contestação requer contraparte autorizada')
        payment = self.payments[number - 1]
        if payment.status is not PaymentStatus.REPORTED_PAID:
            raise RuleError('transição de pagamento inválida')
        payment.status = target
        self._event(actor, f'PAYMENT_{number}_{target.value}')

    def cancel(self, actor: int, *, permitted_by_policy=False):
        self._party(actor)
        if not permitted_by_policy or self.status not in (EngagementStatus.PENDING_AGREEMENT, EngagementStatus.ACTIVE):
            raise RuleError('cancelamento depende de regra de negócio por aprovar')
        self.status = EngagementStatus.CANCELLED
        self._event(actor, 'CANCELLED')