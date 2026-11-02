"""D51: explicit bilateral acceptance on an immutable proposed AgreementVersion."""
import hashlib
import json

from django.db import transaction
from django.shortcuts import get_object_or_404
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
    if request.user.id not in parties:
        return engagement, False
    return engagement, True


def engagement_data(obj):
    versions = obj.agreement_versions.order_by("version").all()
    return {
        "id": obj.id,
        "proposal_id": obj.proposal_id,
        "status": obj.status,
        "worker_user_id": obj.worker_user_id,
        "employer_user_id": obj.employer_user_id,
        "versions": [{
            "id": v.pk,
            "number": v.version,
            "status": v.status,
            "scope": v.scope,
            "amount": str(v.amount) if v.amount is not None else None,
            "price_after_diagnosis": v.price_after_diagnosis,
            "content_fingerprint": v.content_fingerprint,
            "acceptances": list(v.acceptances.values_list("actor_id", flat=True)),
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
    data = AgreementInput(data=request.data)
    data.is_valid(raise_exception=True)
    with transaction.atomic():
        engagement, allowed = _get_engagement(request, engagement_id, lock=True)
        if not allowed:
            return Response({"detail": "Not an engagement party"}, status=403)
        if engagement.status != Engagement.Status.PENDING_AGREEMENT:
            return Response({"detail": "Engagement is already active"}, status=409)
        if engagement.agreement_versions.exists():
            return Response({"detail": "Initial version already exists"}, status=409)

        values = data.validated_data
        version = AgreementVersion.objects.create(
            engagement=engagement,
            version=1,
            scope=values["scope"],
            amount=values.get("amount"),
            price_after_diagnosis=values["price_after_diagnosis"],
            proposed_by=request.user,
            content_fingerprint=fingerprint(
                values["scope"], values.get("amount"), values["price_after_diagnosis"]
            ),
        )
        return Response({
            "version_id": version.id,
            "number": version.version,
            "status": version.status,
            "content_fingerprint": version.content_fingerprint,
            "engagement_status": engagement.status,
        }, status=201)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def accept_agreement(request, engagement_id, version_id):
    with transaction.atomic():
        engagement, allowed = _get_engagement(request, engagement_id, lock=True)
        if not allowed:
            return Response({"detail": "Not an engagement party"}, status=403)
        version = get_object_or_404(
            AgreementVersion.objects.select_for_update(),
            pk=version_id, engagement=engagement,
        )
        if (
            engagement.status != Engagement.Status.PENDING_AGREEMENT
            or version.status != AgreementVersion.Status.PROPOSED
        ):
            return Response({"detail": "Agreement is not pending acceptance"}, status=409)
        if version.content_fingerprint != fingerprint(
            version.scope, version.amount, version.price_after_diagnosis
        ):
            return Response({"detail": "Agreement content mismatch"}, status=409)
        if AgreementAcceptance.objects.filter(
            agreement_version=version, actor=request.user
        ).exists():
            return Response({"detail": "Already accepted"}, status=409)

        AgreementAcceptance.objects.create(
            agreement_version=version,
            actor=request.user,
            content_fingerprint=version.content_fingerprint,
        )
        accepted_actor_ids = set(
            version.acceptances.values_list("actor_id", flat=True)
        )
        parties = {engagement.worker_user_id, engagement.employer_user_id}
        if accepted_actor_ids == parties:
            version.status = AgreementVersion.Status.ACCEPTED
            version.save(update_fields=["status"])
            engagement.status = Engagement.Status.ACTIVE
            engagement.save(update_fields=["status"])
        return Response({
            "engagement_id": engagement.id,
            "agreement_version_id": version.id,
            "agreement_status": version.status,
            "engagement_status": engagement.status,
            "accepted_by": sorted(accepted_actor_ids),
        })
