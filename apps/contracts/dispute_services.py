"""Non-binding, documentary dispute workflow (RN13/RN14/RN16)."""
from django.db import transaction
from django.shortcuts import get_object_or_404
from django.db.models import Q
from rest_framework.exceptions import PermissionDenied

from .models import Contract, Dispute, DisputeEvidence, DisputeEvent
from .services import Conflict, contract_for


def require_admin(actor):
    if not actor.is_authenticated or not actor.is_staff:
        raise PermissionDenied("Só administradores podem actualizar o acompanhamento.")


def add_event(dispute, actor, action, note):
    return DisputeEvent.objects.create(
        dispute=dispute, actor=actor,
        action=action, status_after=dispute.status, note=note,
    )


def accessible_disputes(actor):
    qs = Dispute.objects.select_related(
        "contract__employer", "contract__worker", "reported_by", "requested_from"
    ).prefetch_related("evidence", "events")
    if actor.is_staff:
        return qs
    return qs.filter(
        Q(contract__employer__user=actor) | Q(contract__worker__user=actor)
    )


def accessible_case(pk, actor, lock=False):
    qs = accessible_disputes(actor)
    if lock:
        # Mutation endpoints must not reuse prefetched events/evidence.
        # Otherwise the response serializes stale audit history after add_event().
        qs = qs.prefetch_related(None).select_for_update()
    # 404, rather than exposing identifiers to outsiders.
    return get_object_or_404(qs, pk=pk)


@transaction.atomic
def report_dispute(actor, data):
    contract = contract_for(data["contract_id"], actor, lock=True)
    dispute = Dispute.objects.create(
        contract=contract, reported_by=actor,
        category=data["category"], description=data["description"].strip(),
    )
    DisputeEvidence.objects.create(
        dispute=dispute, author=actor,
        description=data["evidence_description"].strip(),
        url=data.get("evidence_url", ""),
    )
    add_event(
        dispute, actor, "REPORTED",
        "Conflito reportado com categoria e evidência descritiva.",
    )
    return dispute


@transaction.atomic
def add_evidence(case_id, actor, data):
    d = accessible_case(case_id, actor, lock=True)
    if actor.id not in (d.contract.employer.user_id, d.contract.worker.user_id):
        raise PermissionDenied("Só as partes podem acrescentar evidência.")
    if d.status in (Dispute.Status.RESOLVED, Dispute.Status.CLOSED):
        raise Conflict("Este acompanhamento já não recebe evidências.")
    DisputeEvidence.objects.create(
        dispute=d, author=actor,
        description=data["description"].strip(),
        url=data.get("url", ""),
    )
    requested = (
        d.status == Dispute.Status.WAITING_INFORMATION
        and d.requested_from_id == actor.id
    )
    if requested:
        d.status = Dispute.Status.UNDER_REVIEW
        d.requested_from = None
        d.save(update_fields=["status", "requested_from", "updated_at"])
    add_event(
        d, actor,
        "INFORMATION_SUPPLIED" if requested else "EVIDENCE_ADDED",
        "Informação descritiva adicionada pela parte; autenticidade não verificada.",
    )
    return d


@transaction.atomic
def begin_review(case_id, actor, note):
    require_admin(actor)
    d = accessible_case(case_id, actor, lock=True)
    if d.status != Dispute.Status.OPEN:
        raise Conflict("Só uma ocorrência OPEN pode entrar em análise.")
    d.status = Dispute.Status.UNDER_REVIEW
    d.save(update_fields=["status", "updated_at"])
    add_event(d, actor, "REVIEW_STARTED", note)
    return d


@transaction.atomic
def request_information(case_id, actor, recipient_id, note):
    require_admin(actor)
    d = accessible_case(case_id, actor, lock=True)
    if d.status != Dispute.Status.UNDER_REVIEW:
        raise Conflict("É necessário haver análise administrativa em curso.")
    if recipient_id not in (d.contract.employer.user_id, d.contract.worker.user_id):
        raise PermissionDenied("O destinatário deve ser uma parte contratante.")
    d.status = Dispute.Status.WAITING_INFORMATION
    d.requested_from_id = recipient_id
    d.save(update_fields=["status", "requested_from", "updated_at"])
    add_event(d, actor, "INFORMATION_REQUESTED", f"Pedido à parte #{recipient_id}: {note}")
    return d


@transaction.atomic
def register_result(case_id, actor, note):
    require_admin(actor)
    d = accessible_case(case_id, actor, lock=True)
    if d.status != Dispute.Status.UNDER_REVIEW:
        raise Conflict("Só análise em curso pode receber resultado administrativo.")
    d.status = Dispute.Status.RESOLVED
    d.administrative_result = note
    d.requested_from = None
    d.save(update_fields=["status", "administrative_result", "requested_from", "updated_at"])
    add_event(
        d, actor, "ADMINISTRATIVE_RESULT",
        "Resultado administrativo não vinculativo: " + note,
    )
    return d


@transaction.atomic
def close_case(case_id, actor, note):
    require_admin(actor)
    d = accessible_case(case_id, actor, lock=True)
    if d.status != Dispute.Status.RESOLVED:
        raise Conflict("Registe o resultado antes de encerrar o acompanhamento.")
    d.status = Dispute.Status.CLOSED
    d.save(update_fields=["status", "updated_at"])
    add_event(d, actor, "ADMINISTRATIVELY_CLOSED", note)
    return d
