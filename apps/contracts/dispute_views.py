"""Dispute endpoints: participant evidence, non-binding admin review."""
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .dispute_serializers import (
    DisputeReportSerializer, DisputeEvidenceInputSerializer,
    DisputeNoteSerializer, DisputeQuestionSerializer, DisputeResultSerializer,
    DisputeReadSerializer,
)
from .dispute_services import (
    accessible_disputes, accessible_case, report_dispute,
    add_evidence, begin_review, request_information, register_result, close_case,
)


class Disputes(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response(
            DisputeReadSerializer(accessible_disputes(request.user)[:100], many=True).data
        )

    def post(self, request):
        serializer = DisputeReportSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        dispute = report_dispute(request.user, serializer.validated_data)
        return Response(
            DisputeReadSerializer(dispute).data, status=status.HTTP_201_CREATED
        )


class DisputeDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        return Response(
            DisputeReadSerializer(accessible_case(pk, request.user)).data
        )


class DisputeAddEvidence(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        serializer = DisputeEvidenceInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(DisputeReadSerializer(
            add_evidence(pk, request.user, serializer.validated_data)
        ).data)


class DisputeBeginReview(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        serializer = DisputeNoteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(DisputeReadSerializer(
            begin_review(pk, request.user, serializer.validated_data["note"])
        ).data)


class DisputeRequestInformation(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        serializer = DisputeQuestionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(DisputeReadSerializer(request_information(
            pk, request.user, serializer.validated_data["requested_from_user_id"],
            serializer.validated_data["note"],
        )).data)


class DisputeRegisterResult(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        serializer = DisputeResultSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(DisputeReadSerializer(
            register_result(pk, request.user, serializer.validated_data["note"])
        ).data)


class DisputeClose(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        serializer = DisputeNoteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(DisputeReadSerializer(
            close_case(pk, request.user, serializer.validated_data["note"])
        ).data)
