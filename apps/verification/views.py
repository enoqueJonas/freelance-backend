"""Role-scoped evidence review. 'Reviewed' never means identity verified."""
from django.db import IntegrityError, transaction
from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.accounts.models import Employer, Worker
from .models import ProfileEvidenceReview
from .serializers import (
    EvidenceSubmissionSerializer, EvidenceDecisionSerializer,
    EvidenceReviewReadSerializer,
)


class EvidenceReviews(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        records = ProfileEvidenceReview.objects.filter(
            submitted_by=request.user
        ).select_related("reviewed_by")[:100]
        return Response(EvidenceReviewReadSerializer(records, many=True).data)

    def post(self, request):
        serializer = EvidenceSubmissionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        profile_role = data["profile_role"]
        target = (
            Worker.objects.filter(user=request.user).first()
            if profile_role == "worker"
            else Employer.objects.filter(user=request.user).first()
        )
        if target is None:
            return Response(
                {"detail": "Crie o perfil correspondente antes de submeter evidências."},
                status=status.HTTP_403_FORBIDDEN,
            )
        scope = {"worker": target} if profile_role == "worker" else {"employer": target}
        if ProfileEvidenceReview.objects.filter(
            **scope, status=ProfileEvidenceReview.Status.PENDING
        ).exists():
            return Response(
                {"detail": "Existe uma referência pendente para este perfil."},
                status=status.HTTP_409_CONFLICT,
            )
        try:
            with transaction.atomic():
                record = ProfileEvidenceReview.objects.create(
                    **scope, submitted_by=request.user,
                    kind=data["kind"], description=data["description"],
                    reference_url=data["reference_url"],
                )
        except IntegrityError:
            return Response(
                {"detail": "Existe uma referência pendente para este perfil."},
                status=status.HTTP_409_CONFLICT,
            )
        return Response(
            EvidenceReviewReadSerializer(record).data,
            status=status.HTTP_201_CREATED,
        )


class EvidenceReviewDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        qs = ProfileEvidenceReview.objects.all()
        if not request.user.is_staff:
            qs = qs.filter(submitted_by=request.user)
        record = get_object_or_404(qs, pk=pk)
        return Response(EvidenceReviewReadSerializer(record).data)


class PendingEvidenceReviews(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        records = ProfileEvidenceReview.objects.filter(
            status=ProfileEvidenceReview.Status.PENDING
        ).select_related("submitted_by")[:100]
        return Response(EvidenceReviewReadSerializer(records, many=True).data)


class EvidenceReviewDecision(APIView):
    permission_classes = [IsAdminUser]

    def post(self, request, pk):
        serializer = EvidenceDecisionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        with transaction.atomic():
            record = get_object_or_404(
                ProfileEvidenceReview.objects.select_for_update(), pk=pk
            )
            if record.submitted_by_id == request.user.id:
                return Response(
                    {"detail": "Não pode rever uma referência submetida por si."},
                    status=status.HTTP_403_FORBIDDEN,
                )
            if record.status != ProfileEvidenceReview.Status.PENDING:
                return Response(
                    {"detail": "Esta referência já foi analisada."},
                    status=status.HTTP_409_CONFLICT,
                )
            record.status = serializer.validated_data["decision"]
            record.review_note = serializer.validated_data["note"]
            record.reviewed_by = request.user
            record.reviewed_at = timezone.now()
            record.save(update_fields=[
                "status", "review_note", "reviewed_by", "reviewed_at",
            ])
        return Response(EvidenceReviewReadSerializer(record).data)
