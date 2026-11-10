from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.contracts.services import contract_for
from .models import ExternalPayment
from .serializers import (
    ExternalPaymentReadSerializer, ExternalPaymentReportSerializer,
    ExternalPaymentResponseSerializer,
)
from .services import answer_external_payment, declare_external_payment


class ExternalPaymentsForContract(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, contract_id):
        contract = contract_for(contract_id, request.user)
        qs = ExternalPayment.objects.filter(
            contract=contract
        ).prefetch_related("history")
        return Response(ExternalPaymentReadSerializer(qs, many=True).data)

    def post(self, request, contract_id):
        serializer = ExternalPaymentReportSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        payment = declare_external_payment(
            contract_id, request.user, serializer.validated_data
        )
        return Response(
            ExternalPaymentReadSerializer(payment).data,
            status=status.HTTP_201_CREATED,
        )


class ExternalPaymentRespond(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, payment_id):
        serializer = ExternalPaymentResponseSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        payment = answer_external_payment(
            payment_id, request.user, serializer.validated_data
        )
        return Response(ExternalPaymentReadSerializer(payment).data)
