"""D52: initial and amended agreements with versioned bilateral consent.

The three lifecycles (service, dispute, payment) remain independent; this file
only implements proposed/accepted/rejected/superseded agreement versions.
No claim of digital-signature equivalence or production security is made.
"""
import hashlib
import json

from django.db import transaction
from django.db.models import Max
from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework import serializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import AgreementAcceptance, AgreementVersion, Engagement


class AgreementInput(serializers.Serializer):
    scope = serializers.CharField(trim_whitespace=True, allow_blank=False)
    amount = serializers.DecimalField(
        max_digits=12, decimal_places=2, allow_null=True, required=False, min_value=0.01
    )
    price_after_diagnosis = serializers.BooleanField(default=False)

    def validate(self, attrs):
        amount = attrs.get("amount")
        later = attrs["price_after_diagnosis"]
        if (amount is None) == (not later):
            raise serializers.ValidationError(
                "Specify exactly one: amount OR price_after_diagnosis"
            )
        return attrs


class ConsentInput(serializers.Serializer):
    # The caller must explicitly confirm the same content it actually reviewed.
    content_fingerprint = serializers.RegexField(r"^[0-9a-f]{64}$")


class RejectionInput(ConsentInput):
    reason = serializers.CharField(max_length=500, allow_blank=False, trim_whitespace=True)


def fingerprint(scope, amount, later):
    payload = {
        "scope": scope,
        "amount": str(amount) if amount is not None else None,
        "price_after_diagnosis": later,
    }
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()


def _get_engagement(request, engagement_id, *, lock=False):
    qs = Engagement.objects.select_related(
        "proposal__worker", "proposal__opportunity__employer"
    )
    if lock:
        qs = qs.select_for_update()
    engagement = get_object_or_404(qs, pk=engagement_id)
    parties = {engagement.worker_user_id, engagement.employer_user_id}
    return engagement, request.user.id in parties


def _verify_current_content(version, supplied_fingerprint):
    actual = fingerprint(version.scope, version.amount, version.price_after_diagnosis)
    return version.content_fingerprint == actual == supplied_fingerprint


def engagement_data(obj):
    versions = list(
        obj.agreement_versions.select_related("proposed_by", "rejected_by")
        .prefetch_related("acceptances")
        .order_by("version")
    )
    current = next((v for v in versions if v.status == AgreementVersion.Status.ACCEPTED), None)
    return {
        "id": obj.id,
        "proposal_id": obj.proposal_id,
        "status": obj.status,
        "worker_user_id": obj.worker_user_id,
        "employer_user_id": obj.employer_user_id,
        "current_agreement_version_id": current.pk if current else None,
        "versions": [{
            "id": v.pk,
            "number": v.version,
            "status": v.status,
            "is_current": current is not None and v.pk == current.pk,
            "scope": v.scope,
            "amount": str(v.amount) if v.amount is not None else None,
            "price_after_diagnosis": v.price_after_diagnosis,
            "content_fingerprint": v.content_fingerprint,
            "proposed_by_user_id": v.proposed_by_id,
            "rejected_by_user_id": v.rejected_by_id,
            "rejected_at": v.rejected_at.isoformat() if v.rejected_at else None,
            "rejection_reason": v.rejection_reason,
            "acceptances": sorted(a.actor_id for a in v.acceptances.all()),
        } for v in versions],
    }


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def engagement_detail(request, engagement_id):
    obj, allowed = _get_engagement(request, engagement_id)
    if not allowed:
        return Response({"detail": "Only engagement parties can view it"}, status=403)
    return Response(engagement_data(obj))


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def propose_initial_agreement(request, engagement_id):
    """Create v1 or vN+1; an accepted version remains current until bilateral consent."""
    payload = AgreementInput(data=request.data)
    payload.is_valid(raise_exception=True)
    with transaction.atomic():
        engagement, allowed = _get_engagement(request, engagement_id, lock=True)
        if not allowed:
            return Response({"detail": "Not an engagement party"}, status=403)
        if engagement.status not in (
            Engagement.Status.PENDING_AGREEMENT,
            Engagement.Status.ACTIVE,
        ):
            return Response({"detail": "Engagement not eligible for agreement"}, status=409)
        versions = engagement.agreement_versions
        if versions.filter(status=AgreementVersion.Status.PROPOSED).exists():
            return Response({"detail": "Another version is awaiting decision"}, status=409)
        current_exists = versions.filter(status=AgreementVersion.Status.ACCEPTED).exists()
        if engagement.status == Engagement.Status.ACTIVE and not current_exists:
            return Response({"detail": "Active engagement lacks a current agreement"}, status=409)
        if engagement.status == Engagement.Status.PENDING_AGREEMENT and current_exists:
            return Response({"detail": "Pending engagement has a current agreement"}, status=409)

        next_version = (versions.aggregate(last=Max("version"))["last"] or 0) + 1
        data = payload.validated_data
        new_version = AgreementVersion.objects.create(
            engagement=engagement,
            version=next_version,
            scope=data["scope"],
            amount=data.get("amount"),
            price_after_diagnosis=data["price_after_diagnosis"],
            proposed_by=request.user,
            content_fingerprint=fingerprint(
                data["scope"], data.get("amount"), data["price_after_diagnosis"]
            ),
        )
        return Response({
            "version_id": new_version.pk,
            "number": new_version.version,
            "status": new_version.status,
            "content_fingerprint": new_version.content_fingerprint,
            "engagement_status": engagement.status,
        }, status=201)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def accept_agreement(request, engagement_id, version_id):
    consent = ConsentInput(data=request.data)
    consent.is_valid(raise_exception=True)
    with transaction.atomic():
        engagement, allowed = _get_engagement(request, engagement_id, lock=True)
        if not allowed:
            return Response({"detail": "Not an engagement party"}, status=403)
        version = get_object_or_404(
            AgreementVersion.objects.select_for_update(), pk=version_id, engagement=engagement,
        )
        if (
            engagement.status not in (Engagement.Status.PENDING_AGREEMENT, Engagement.Status.ACTIVE)
            or version.status != AgreementVersion.Status.PROPOSED
        ):
            return Response({"detail": "Agreement is not pending acceptance"}, status=409)
        if not _verify_current_content(version, consent.validated_data["content_fingerprint"]):
            return Response({"detail": "Agreement content or fingerprint mismatch"}, status=409)
        if AgreementAcceptance.objects.filter(
            agreement_version=version, actor=request.user
        ).exists():
            return Response({"detail": "Already accepted"}, status=409)

        AgreementAcceptance.objects.create(
            agreement_version=version,
            actor=request.user,
            content_fingerprint=version.content_fingerprint,
        )
        accepted_actor_ids = set(version.acceptances.values_list("actor_id", flat=True))
        parties = {engagement.worker_user_id, engagement.employer_user_id}
        if accepted_actor_ids == parties:
            # One transaction: the previous accepted agreement is superseded, vN becomes
            # current, and the engagement is activated if it was still pending.
            AgreementVersion.objects.filter(
                engagement=engagement, status=AgreementVersion.Status.ACCEPTED
            ).update(status=AgreementVersion.Status.SUPERSEDED)
            version.status = AgreementVersion.Status.ACCEPTED
            version.save(update_fields=["status"])
            if engagement.status == Engagement.Status.PENDING_AGREEMENT:
                engagement.status = Engagement.Status.ACTIVE
                engagement.save(update_fields=["status"])
        return Response({
            "engagement_id": engagement.pk,
            "agreement_version_id": version.pk,
            "agreement_status": version.status,
            "engagement_status": engagement.status,
            "accepted_by": sorted(accepted_actor_ids),
            "current_agreement_version_id": (
                version.pk
                if version.status == AgreementVersion.Status.ACCEPTED
                else engagement.agreement_versions.filter(
                    status=AgreementVersion.Status.ACCEPTED
                ).values_list("pk", flat=True).first()
            ),
        })


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def reject_agreement(request, engagement_id, version_id):
    rejection = RejectionInput(data=request.data)
    rejection.is_valid(raise_exception=True)
    with transaction.atomic():
        engagement, allowed = _get_engagement(request, engagement_id, lock=True)
        if not allowed:
            return Response({"detail": "Not an engagement party"}, status=403)
        version = get_object_or_404(
            AgreementVersion.objects.select_for_update(), pk=version_id, engagement=engagement,
        )
        if version.status != AgreementVersion.Status.PROPOSED:
            return Response({"detail": "Only proposed versions may be rejected"}, status=409)
        if version.proposed_by_id == request.user.id:
            return Response({
                "detail": "Proponent cannot reject own version; withdrawal is a separate decision"
            }, status=403)
        if not _verify_current_content(version, rejection.validated_data["content_fingerprint"]):
            return Response({"detail": "Agreement content or fingerprint mismatch"}, status=409)

        version.status = AgreementVersion.Status.REJECTED
        version.rejected_by = request.user
        version.rejected_at = timezone.now()
        version.rejection_reason = rejection.validated_data["reason"]
        version.save(update_fields=["status", "rejected_by", "rejected_at", "rejection_reason"])
        current = engagement.agreement_versions.filter(
            status=AgreementVersion.Status.ACCEPTED
        ).values_list("pk", flat=True).first()
        return Response({
            "agreement_version_id": version.pk,
            "agreement_status": version.status,
            "engagement_status": engagement.status,
            "current_agreement_version_id": current,
        })
