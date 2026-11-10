"""Authenticated contract endpoints: no client-chosen owners or status flags."""
from django.db.models import Q
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import AgreementVersion, Contract
from .serializers import (
    AgreementDraftInputSerializer, AgreementVersionReadSerializer,
    ContractReadSerializer, ReasonSerializer,
)
from .services import (
    accept_proposal, approve_version, complete_contract, contract_for,
    open_amendment, reject_version, renegotiate_initial,
    save_draft, submit_draft,
)


class AcceptProposal(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, proposal_id):
        contract, draft = accept_proposal(proposal_id, request.user)
        return Response({
            "contract": ContractReadSerializer(contract).data,
            "draft": AgreementVersionReadSerializer(draft).data,
        }, status=status.HTTP_201_CREATED)


class MyContracts(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        contracts = Contract.objects.filter(
            Q(employer__user=request.user) |
            Q(worker__user=request.user)
        ).select_related("employer", "worker")[:100]
        return Response(ContractReadSerializer(contracts, many=True).data)


class ContractDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, contract_id):
        return Response(
            ContractReadSerializer(contract_for(contract_id, request.user)).data
        )


class AgreementVersions(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, contract_id):
        contract = contract_for(contract_id, request.user)
        versions = AgreementVersion.objects.filter(
            contract=contract
        ).select_related("created_by").prefetch_related("approvals", "events")
        return Response(AgreementVersionReadSerializer(versions, many=True).data)


class AgreementDraftEdit(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request, version_id):
        serializer = AgreementDraftInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        version = save_draft(version_id, request.user, serializer.validated_data["terms"])
        return Response(AgreementVersionReadSerializer(version).data)


class AgreementSubmit(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, version_id):
        version = submit_draft(version_id, request.user)
        return Response(AgreementVersionReadSerializer(version).data)


class AgreementApprove(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, version_id):
        version = approve_version(version_id, request.user)
        return Response(AgreementVersionReadSerializer(version).data)


class AgreementReject(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, version_id):
        serializer = ReasonSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        version = reject_version(version_id, request.user, serializer.validated_data["reason"])
        return Response(AgreementVersionReadSerializer(version).data)


class AgreementAmend(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, contract_id):
        serializer = ReasonSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        version = open_amendment(
            contract_id, request.user, serializer.validated_data["reason"]
        )
        return Response(
            AgreementVersionReadSerializer(version).data,
            status=status.HTTP_201_CREATED,
        )


class AgreementRenegotiate(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, contract_id):
        serializer = ReasonSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        version = renegotiate_initial(
            contract_id, request.user, serializer.validated_data["reason"]
        )
        return Response(
            AgreementVersionReadSerializer(version).data,
            status=status.HTTP_201_CREATED,
        )


class ContractComplete(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, contract_id):
        contract = complete_contract(contract_id, request.user)
        return Response(ContractReadSerializer(contract).data)
