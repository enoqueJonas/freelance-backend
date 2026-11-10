"""Transactional declarations of *external* payment, no transfer or escrow."""
from decimal import Decimal, InvalidOperation

from django.db import transaction
from django.db.models import Sum
from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework.exceptions import PermissionDenied, ValidationError

from apps.contracts.models import AgreementVersion, Contract
from apps.contracts.services import Conflict, contract_for

from .models import ExternalPayment, ExternalPaymentEvent


COUNTED = [ExternalPayment.Status.REPORTED_PAID, ExternalPayment.Status.CONFIRMED]


def add_event(payment, actor, note):
    return ExternalPaymentEvent.objects.create(
        payment=payment, actor=actor, status_after=payment.status, note=note
    )


@transaction.atomic
def declare_external_payment(contract_id, actor, data):
    contract = contract_for(contract_id, actor, lock=True)
    if contract.employer.user_id != actor.id:
        raise PermissionDenied("Só o empregador pode declarar pagamentos externos.")
    if contract.status not in (Contract.Status.ACTIVE, Contract.Status.COMPLETED):
        raise Conflict("O contrato tem de estar activo ou concluído.")
    if data["paid_on"] > timezone.localdate():
        raise ValidationError({"paid_on": "Não pode ser uma data futura."})

    version = AgreementVersion.objects.select_for_update().filter(
        contract=contract, status=AgreementVersion.Status.ACTIVE
    ).first()
    if version is None:
        raise Conflict("É necessário um acordo bilateral aceite.")
    condition = next(
        (item for item in version.terms.get("payment_conditions", [])
         if item.get("id") == data["agreement_condition_id"]),
        None,
    )
    if condition is None or any([
        condition.get("method") != data["method"],
        condition.get("stage") != data["stage"],
        condition.get("moment") != data["moment"].strip(),
    ]):
        raise ValidationError(
            {"agreement_condition_id": "A declaração não corresponde à condição vigente."}
        )
    try:
        ceiling = Decimal(str(condition["amount"]))
    except (InvalidOperation, KeyError, TypeError, ValueError):
        raise Conflict("O acordo activo contém uma etapa de pagamento inválida.")

    used_stage = ExternalPayment.objects.filter(
        contract=contract, agreement_version=version,
        agreement_condition_id=data["agreement_condition_id"],
        status__in=COUNTED,
    ).aggregate(total=Sum("amount"))["total"] or Decimal("0.00")
    if used_stage + data["amount"] > ceiling:
        raise ValidationError({"amount": "Excede a etapa aprovada."})

    used_contract = ExternalPayment.objects.filter(
        contract=contract, status__in=COUNTED,
    ).aggregate(total=Sum("amount"))["total"] or Decimal("0.00")
    if used_contract + data["amount"] > contract.budget:
        raise ValidationError({"amount": "Excede o orçamento contratual."})

    payment = ExternalPayment.objects.create(
        contract=contract, agreement_version=version,
        agreement_condition_id=data["agreement_condition_id"],
        amount=data["amount"], method=data["method"], stage=data["stage"],
        moment=data["moment"].strip(), paid_on=data["paid_on"],
        external_reference=data.get("external_reference", "").strip(),
        notes=data.get("notes", "").strip(),
        reported_by=actor,
    )
    add_event(
        payment, actor,
        "O empregador declarou um pagamento externo; a plataforma não verificou transferências.",
    )
    return payment


@transaction.atomic
def answer_external_payment(payment_id, actor, data):
    original = get_object_or_404(ExternalPayment, pk=payment_id)
    contract = contract_for(original.contract_id, actor, lock=True)
    if contract.worker.user_id != actor.id or contract.employer.user_id == actor.id:
        raise PermissionDenied("Só o trabalhador pode responder à declaração.")
    payment = get_object_or_404(
        ExternalPayment.objects.select_for_update(), pk=payment_id
    )
    if payment.status != ExternalPayment.Status.REPORTED_PAID:
        raise Conflict("Este registo já foi confirmado ou contestado.")
    payment.status = data["action"]
    payment.responded_by = actor
    payment.response_note = (
        data.get("reason", "").strip()
        if data["action"] == ExternalPayment.Status.CONTESTED
        else "O trabalhador declarou ter recebido o montante; sem verificação bancária."
    )
    payment.save(update_fields=[
        "status", "responded_by", "response_note", "updated_at"
    ])
    add_event(payment, actor, payment.response_note)
    return payment
