"""Agreement validation and read-only audit representations."""
import json
from decimal import Decimal

from django.core.serializers.json import DjangoJSONEncoder
from rest_framework import serializers

from .models import AgreementApproval, AgreementEvent, AgreementVersion, Contract


class PaymentConditionSerializer(serializers.Serializer):
    id = serializers.CharField(min_length=1, max_length=64)
    stage = serializers.ChoiceField(choices=["ADVANCE", "MILESTONE", "FINAL"])
    amount = serializers.DecimalField(
        max_digits=12, decimal_places=2, min_value=Decimal("0.01")
    )
    method = serializers.ChoiceField(
        choices=["M-Pesa", "e-Mola", "Transferência Bancária", "Outro"]
    )
    moment = serializers.CharField(min_length=8, max_length=300)


class AgreementTermsSerializer(serializers.Serializer):
    title = serializers.CharField(min_length=5, max_length=180)
    scope = serializers.CharField(min_length=20, max_length=8000)
    deliverables = serializers.CharField(min_length=12, max_length=5000)
    acceptance_criteria = serializers.CharField(min_length=15, max_length=5000)
    budget = serializers.DecimalField(
        max_digits=12, decimal_places=2, min_value=Decimal("0.01")
    )
    start_date = serializers.DateField()
    end_date = serializers.DateField()
    payment_conditions = PaymentConditionSerializer(many=True, allow_empty=False)

    def validate(self, attrs):
        if attrs["end_date"] < attrs["start_date"]:
            raise serializers.ValidationError({
                "end_date": "O fim não pode anteceder o início."
            })
        conditions = attrs["payment_conditions"]
        if len(conditions) > 12:
            raise serializers.ValidationError({
                "payment_conditions": "Máximo de doze etapas."
            })
        identifiers = [step["id"] for step in conditions]
        if len(identifiers) != len(set(identifiers)):
            raise serializers.ValidationError({
                "payment_conditions": "As etapas têm de possuir IDs distintos."
            })
        total = sum((step["amount"] for step in conditions), Decimal("0.00"))
        if total != attrs["budget"]:
            raise serializers.ValidationError({
                "payment_conditions": "A soma deve corresponder ao orçamento."
            })
        return attrs


def validate_published_terms(raw_terms):
    serializer = AgreementTermsSerializer(data=raw_terms)
    serializer.is_valid(raise_exception=True)
    # Django JSONField must store plain serializable types (Decimal -> string).
    return json.loads(json.dumps(serializer.validated_data, cls=DjangoJSONEncoder))


class AgreementDraftInputSerializer(serializers.Serializer):
    terms = serializers.JSONField()

    def validate_terms(self, value):
        if not isinstance(value, dict):
            raise serializers.ValidationError("O acordo deve ser um objeto.")
        if len(json.dumps(value, ensure_ascii=False)) > 25000:
            raise serializers.ValidationError("O rascunho é demasiado grande.")
        allowed = {
            "title", "scope", "deliverables", "acceptance_criteria",
            "budget", "start_date", "end_date", "payment_conditions",
        }
        if set(value) - allowed:
            raise serializers.ValidationError("Existem campos não permitidos.")
        return value


class ReasonSerializer(serializers.Serializer):
    reason = serializers.CharField(min_length=8, max_length=1000)


class AgreementApprovalReadSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = AgreementApproval
        fields = ["id", "party", "user_id", "approved_at"]
        read_only_fields = fields


class AgreementEventReadSerializer(serializers.ModelSerializer):
    actor_user_id = serializers.IntegerField(source="actor_id", read_only=True)

    class Meta:
        model = AgreementEvent
        fields = ["id", "action", "status_after", "actor_user_id", "note", "recorded_at"]
        read_only_fields = fields


class AgreementVersionReadSerializer(serializers.ModelSerializer):
    approvals = AgreementApprovalReadSerializer(many=True, read_only=True)
    events = AgreementEventReadSerializer(many=True, read_only=True)
    created_by_user_id = serializers.IntegerField(
        source="created_by_id", read_only=True
    )

    class Meta:
        model = AgreementVersion
        fields = [
            "id", "contract_id", "number", "status", "reason", "terms",
            "created_by_user_id", "submitted_at", "rejected_by_id",
            "rejection_reason", "created_at", "approvals", "events",
        ]
        read_only_fields = fields


class ContractReadSerializer(serializers.ModelSerializer):
    employer_user_id = serializers.IntegerField(source="employer.user_id", read_only=True)
    worker_user_id = serializers.IntegerField(source="worker.user_id", read_only=True)

    class Meta:
        model = Contract
        fields = [
            "id", "offer_id", "proposal_id", "employer_user_id",
            "worker_user_id", "title", "scope", "budget",
            "start_date", "end_date", "status", "created_at", "updated_at",
        ]
        read_only_fields = fields
