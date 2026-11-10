"""Atomic contract and agreement transitions. Ownership is determined on the server."""
from django.db import IntegrityError, transaction
from django.db.models import Max
from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework.exceptions import APIException, PermissionDenied, ValidationError

from apps.marketplace.models import Offer, Proposal

from .models import AgreementApproval, AgreementEvent, AgreementVersion, Contract
from .serializers import validate_published_terms


class Conflict(APIException):
    status_code = 409
    default_detail = "O estado actual não permite esta operação."
    default_code = "conflict"


def party_of(contract, user):
    if not user or not user.is_authenticated:
        raise PermissionDenied("Autenticação necessária.")
    if contract.employer.user_id == contract.worker.user_id:
        raise Conflict("Contrato inválido: as partes devem ser contas distintas.")
    if contract.employer.user_id == user.id:
        return AgreementApproval.Party.EMPLOYER
    if contract.worker.user_id == user.id:
        return AgreementApproval.Party.WORKER
    raise PermissionDenied("Não pertence a esta contratação.")


def add_event(version, user, action, note):
    return AgreementEvent.objects.create(
        version=version,
        actor=user,
        action=action,
        status_after=version.status,
        note=note,
    )


def contract_for(pk, user, lock=False):
    qs = Contract.objects.select_related(
        "employer", "worker", "employer__user", "worker__user"
    )
    if lock:
        qs = qs.select_for_update()
    contract = get_object_or_404(qs, pk=pk)
    party_of(contract, user)
    return contract


def version_for(pk, user, lock=False):
    qs = AgreementVersion.objects.select_related(
        "contract__employer", "contract__worker", "created_by"
    )
    if lock:
        qs = qs.select_for_update()
    version = get_object_or_404(qs, pk=pk)
    party_of(version.contract, user)
    return version


@transaction.atomic
def accept_proposal(proposal_id, user):
    proposal = get_object_or_404(
        Proposal.objects.select_for_update().select_related(
            "offer__employer", "worker", "worker__user"
        ),
        pk=proposal_id,
    )
    offer = get_object_or_404(
        Offer.objects.select_for_update().select_related("employer"),
        pk=proposal.offer_id,
    )
    if offer.employer.user_id != user.id:
        raise PermissionDenied("Só o empregador pode aceitar esta proposta.")
    if proposal.worker.user_id == user.id:
        raise PermissionDenied("RN02: as duas partes não podem ser a mesma conta.")
    if proposal.status != Proposal.Status.PENDING or offer.status != Offer.Status.ACTIVE:
        raise Conflict("A proposta ou oportunidade já não está disponível.")
    if Contract.objects.filter(offer_id=offer.id).exists():
        raise Conflict("Já existe uma contratação para esta oportunidade.")

    contract = Contract.objects.create(
        offer=offer, proposal=proposal,
        employer=offer.employer, worker=proposal.worker,
        title=offer.title, scope=offer.description,
        budget=proposal.proposed_amount,
        status=Contract.Status.PENDING,
    )
    draft = AgreementVersion.objects.create(
        contract=contract,
        number=1, status=AgreementVersion.Status.DRAFT,
        created_by=user,
        reason="Formalização inicial a partir da proposta aceite.",
        terms={
            "title": offer.title,
            "scope": offer.description,
            "deliverables": "",
            "acceptance_criteria": "",
            "budget": str(proposal.proposed_amount),
            "start_date": "",
            "end_date": "",
            "payment_conditions": [],
        },
    )
    add_event(draft, user, "CREATED", "Rascunho inicial; sem aprovações presumidas.")
    proposal.status = Proposal.Status.ACCEPTED
    proposal.save(update_fields=["status"])
    Proposal.objects.filter(
        offer=offer, status=Proposal.Status.PENDING
    ).exclude(pk=proposal.id).update(status=Proposal.Status.REJECTED)
    offer.status = Offer.Status.CLOSED
    offer.save(update_fields=["status", "updated_at"])
    return contract, draft


@transaction.atomic
def save_draft(version_id, user, raw_terms):
    version = version_for(version_id, user, lock=True)
    if version.status != AgreementVersion.Status.DRAFT or version.created_by_id != user.id:
        raise Conflict("Só o autor pode editar um rascunho não publicado.")
    version.terms = raw_terms
    version.save(update_fields=["terms"])
    add_event(version, user, "DRAFT_UPDATED", "Rascunho actualizado, sem efeito contratual.")
    return version


@transaction.atomic
def submit_draft(version_id, user):
    version = version_for(version_id, user, lock=True)
    if version.status != AgreementVersion.Status.DRAFT or version.created_by_id != user.id:
        raise Conflict("Só o autor pode publicar o seu rascunho.")
    if version.contract.status == Contract.Status.COMPLETED:
        raise Conflict("A contratação já foi concluída.")
    version.terms = validate_published_terms(version.terms)
    version.status = AgreementVersion.Status.PENDING_APPROVAL
    version.submitted_at = timezone.now()
    version.save(update_fields=["terms", "status", "submitted_at"])
    add_event(version, user, "SUBMITTED", "Termos publicados para aceitação bilateral.")
    return version


@transaction.atomic
def approve_version(version_id, user):
    # Lock the contract first: two simultaneous approvals cannot each activate
    # a different version, and budget state is only changed under this lock.
    initial = get_object_or_404(AgreementVersion, pk=version_id)
    contract = contract_for(initial.contract_id, user, lock=True)
    version = version_for(version_id, user, lock=True)
    role = party_of(contract, user)
    if version.status != AgreementVersion.Status.PENDING_APPROVAL:
        raise Conflict("A versão não está disponível para aprovação.")
    if contract.status == Contract.Status.COMPLETED:
        raise Conflict("A contratação já terminou.")
    if AgreementApproval.objects.filter(version=version, party=role).exists():
        raise Conflict("Esta parte já aprovou a versão.")

    AgreementApproval.objects.create(version=version, party=role, user=user)
    add_event(version, user, "APPROVED", f"Aceitação explícita pela parte {role}.")

    approvals = set(version.approvals.values_list("party", flat=True))
    if approvals == {AgreementApproval.Party.EMPLOYER, AgreementApproval.Party.WORKER}:
        # An amendment may not undercut external amounts already declared.
        # The final approval and the check run inside one database transaction,
        # protected by the locked Contract row used by payment declarations.
        from decimal import Decimal
        from django.db.models import Sum
        from apps.payments.models import ExternalPayment

        declared = ExternalPayment.objects.filter(
            contract=contract,
            status__in=[
                ExternalPayment.Status.REPORTED_PAID,
                ExternalPayment.Status.CONFIRMED,
            ],
        ).aggregate(total=Sum("amount"))["total"] or Decimal("0.00")
        if declared > Decimal(str(version.terms["budget"])):
            raise Conflict(
                "Uma nova versão não pode ter valor inferior aos pagamentos declarados."
            )
        old = AgreementVersion.objects.select_for_update().filter(
            contract=contract, status=AgreementVersion.Status.ACTIVE
        ).exclude(pk=version.pk).first()
        if old:
            old.status = AgreementVersion.Status.SUPERSEDED
            old.save(update_fields=["status"])
            add_event(old, user, "SUPERSEDED", f"Substituída por v{version.number}.")
        version.status = AgreementVersion.Status.ACTIVE
        version.save(update_fields=["status"])
        add_event(version, user, "ACTIVATED", "Aprovada pelas duas partes.")
        terms = version.terms
        contract.title = terms["title"]
        contract.scope = terms["scope"]
        contract.budget = terms["budget"]
        contract.start_date = terms["start_date"]
        contract.end_date = terms["end_date"]
        contract.status = Contract.Status.ACTIVE
        contract.save(update_fields=[
            "title", "scope", "budget", "start_date", "end_date", "status", "updated_at"
        ])
    return version


@transaction.atomic
def reject_version(version_id, user, reason):
    initial = get_object_or_404(AgreementVersion, pk=version_id)
    contract_for(initial.contract_id, user, lock=True)
    version = version_for(version_id, user, lock=True)
    if version.status != AgreementVersion.Status.PENDING_APPROVAL:
        raise Conflict("Só versões pendentes podem ser recusadas.")
    version.status = AgreementVersion.Status.REJECTED
    version.rejected_by = user
    version.rejection_reason = reason
    version.save(update_fields=["status", "rejected_by", "rejection_reason"])
    add_event(version, user, "REJECTED", reason)
    return version


def _new_draft(contract, user, reason, previous):
    next_number = (AgreementVersion.objects.filter(
        contract=contract
    ).aggregate(last=Max("number"))["last"] or 0) + 1
    version = AgreementVersion.objects.create(
        contract=contract,
        number=next_number,
        status=AgreementVersion.Status.DRAFT,
        created_by=user,
        reason=reason,
        terms=dict(previous.terms),
    )
    add_event(version, user, "CREATED", reason)
    return version


@transaction.atomic
def open_amendment(contract_id, user, reason):
    contract = contract_for(contract_id, user, lock=True)
    if contract.status != Contract.Status.ACTIVE:
        raise Conflict("Só contratos activos podem receber alterações.")
    if AgreementVersion.objects.filter(
        contract=contract,
        status__in=[AgreementVersion.Status.DRAFT, AgreementVersion.Status.PENDING_APPROVAL],
    ).exists():
        raise Conflict("Já existe uma versão em negociação.")
    current = AgreementVersion.objects.filter(
        contract=contract, status=AgreementVersion.Status.ACTIVE
    ).first()
    if not current:
        raise Conflict("O contrato não possui versão bilateral aceite.")
    return _new_draft(contract, user, reason, current)


@transaction.atomic
def renegotiate_initial(contract_id, user, reason):
    contract = contract_for(contract_id, user, lock=True)
    if contract.status != Contract.Status.PENDING:
        raise Conflict("Esta negociação inicial já terminou.")
    recent = AgreementVersion.objects.filter(contract=contract).order_by("-number").first()
    if recent is None or recent.status != AgreementVersion.Status.REJECTED:
        raise Conflict("Só uma versão inicial recusada pode ser renegociada.")
    return _new_draft(contract, user, reason, recent)


@transaction.atomic
def complete_contract(contract_id, user):
    contract = contract_for(contract_id, user, lock=True)
    if contract.employer.user_id != user.id:
        raise PermissionDenied("Só o empregador pode concluir esta contratação.")
    if contract.status != Contract.Status.ACTIVE:
        raise Conflict("A contratação não está activa.")
    if not AgreementVersion.objects.filter(
        contract=contract, status=AgreementVersion.Status.ACTIVE
    ).exists():
        raise Conflict("O acordo bilateral ainda não está aceite.")
    contract.status = Contract.Status.COMPLETED
    contract.save(update_fields=["status", "updated_at"])
    return contract
