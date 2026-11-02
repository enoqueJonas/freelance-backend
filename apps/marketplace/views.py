"""D51: minimal real Django workflow for opportunities and proposals.

Scope intentionally excludes notifications, chat, payments and delivery.
"""
from django.db import transaction
from django.db.models import Q
from django.shortcuts import get_object_or_404
from rest_framework import serializers, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.accounts.models import Employer, Worker
from .models import Opportunity, Proposal
from apps.contracts.models import Engagement


class OpportunityInput(serializers.Serializer):
    title = serializers.CharField(max_length=160, allow_blank=False, trim_whitespace=True)
    description = serializers.CharField(allow_blank=False, trim_whitespace=True)


class ProposalInput(serializers.Serializer):
    description = serializers.CharField(allow_blank=False, trim_whitespace=True)


def opportunity_data(obj):
    return {
        "id": obj.id,
        "employer_user_id": obj.employer.user_id,
        "title": obj.title,
        "description": obj.description,
        "status": obj.status,
    }


@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def opportunities(request):
    if request.method == "GET":
        qs = (
            Opportunity.objects.select_related("employer")
            .filter(Q(status=Opportunity.Status.OPEN) | Q(employer__user=request.user))
            .distinct()
            .order_by("-created_at")
        )
        return Response([opportunity_data(o) for o in qs])

    employer = Employer.objects.filter(user=request.user).first()
    if not employer:
        return Response({"detail": "Employer profile required"}, status=403)
    input_data = OpportunityInput(data=request.data)
    input_data.is_valid(raise_exception=True)
    obj = Opportunity.objects.create(employer=employer, **input_data.validated_data)
    return Response(opportunity_data(obj), status=status.HTTP_201_CREATED)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def publish_opportunity(request, opportunity_id):
    with transaction.atomic():
        obj = get_object_or_404(
            Opportunity.objects.select_for_update().select_related("employer"),
            pk=opportunity_id,
        )
        if obj.employer.user_id != request.user.id:
            return Response({"detail": "Not an owner"}, status=403)
        if obj.status != Opportunity.Status.DRAFT:
            return Response({"detail": "Only draft opportunities can be published"}, status=409)
        obj.status = Opportunity.Status.OPEN
        obj.save(update_fields=["status"])
        return Response(opportunity_data(obj))


@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def submit_proposal(request, opportunity_id):
    if request.method == "GET":
        obj = get_object_or_404(
            Opportunity.objects.select_related("employer"), pk=opportunity_id
        )
        if obj.employer.user_id != request.user.id:
            return Response({"detail": "Not an owner"}, status=403)
        proposals = (
            Proposal.objects.filter(opportunity=obj)
            .select_related("worker__user")
            .order_by("created_at", "pk")
        )
        return Response([{
            "id": p.pk,
            "opportunity_id": p.opportunity_id,
            "worker_user_id": p.worker.user_id,
            "worker_name": p.worker.user.name,
            "description": p.description,
            "status": p.status,
        } for p in proposals])

    input_data = ProposalInput(data=request.data)
    input_data.is_valid(raise_exception=True)
    worker = Worker.objects.filter(user=request.user).first()
    if worker is None:
        return Response({"detail": "Worker profile required"}, status=403)

    with transaction.atomic():
        obj = get_object_or_404(
            Opportunity.objects.select_for_update().select_related("employer"),
            pk=opportunity_id,
        )
        if obj.employer.user_id == request.user.id:
            return Response({"detail": "Self-contracting is not allowed"}, status=403)
        if obj.status != Opportunity.Status.OPEN:
            return Response({"detail": "Opportunity is not open"}, status=409)
        if Proposal.objects.filter(opportunity=obj, worker=worker).exists():
            return Response({"detail": "Proposal already exists"}, status=409)
        proposal = Proposal.objects.create(
            opportunity=obj, worker=worker, **input_data.validated_data
        )
        return Response({
            "id": proposal.id,
            "status": proposal.status,
            "opportunity_id": obj.id,
            "worker_user_id": request.user.id,
        }, status=201)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def accept_proposal(request, proposal_id):
    with transaction.atomic():
        proposal = get_object_or_404(
            Proposal.objects.select_related("opportunity__employer", "worker"),
            pk=proposal_id,
        )
        obj = get_object_or_404(
            Opportunity.objects.select_for_update().select_related("employer"),
            pk=proposal.opportunity_id,
        )
        if obj.employer.user_id != request.user.id:
            return Response({"detail": "Not an owner"}, status=403)
        if (
            obj.status != Opportunity.Status.OPEN
            or proposal.status != Proposal.Status.SUBMITTED
            or Engagement.objects.filter(proposal__opportunity=obj).exists()
        ):
            return Response({"detail": "Proposal is not selectable"}, status=409)
        if proposal.worker.user_id == request.user.id:
            return Response({"detail": "Self-contracting is not allowed"}, status=403)

        proposal.status = Proposal.Status.ACCEPTED
        proposal.save(update_fields=["status"])
        Proposal.objects.filter(
            opportunity=obj, status=Proposal.Status.SUBMITTED
        ).exclude(pk=proposal.pk).update(status=Proposal.Status.REJECTED)
        obj.status = Opportunity.Status.CLOSED
        obj.save(update_fields=["status"])
        engagement = Engagement.objects.create(proposal=proposal)
        return Response({
            "engagement_id": engagement.id,
            "proposal_id": proposal.id,
            "engagement_status": engagement.status,
        }, status=201)
