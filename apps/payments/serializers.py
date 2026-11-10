"""External payment reports are statements by the parties, not bank confirmations."""
from decimal import Decimal
from rest_framework import serializers

from .models import ExternalPayment, ExternalPaymentEvent


class ExternalPaymentReportSerializer(serializers.Serializer):
    amount = serializers.DecimalField(max_digits=12, decimal_places=2, min_value=Decimal("0.01"))
    method = serializers.ChoiceField(choices=ExternalPayment.Method.choices)
    stage = serializers.ChoiceField(choices=ExternalPayment.Stage.choices)
    moment = serializers.CharField(min_length=8, max_length=300)
    paid_on = serializers.DateField()
    agreement_condition_id = serializers.CharField(min_length=1, max_length=64)
    external_reference = serializers.CharField(max_length=200, required=False, allow_blank=True)
    notes = serializers.CharField(max_length=2000, required=False, allow_blank=True)


class ExternalPaymentResponseSerializer(serializers.Serializer):
    action = serializers.ChoiceField(
        choices=[ExternalPayment.Status.CONFIRMED, ExternalPayment.Status.CONTESTED]
    )
    reason = serializers.CharField(
        max_length=2000, required=False, allow_blank=True
    )

    def validate(self, attrs):
        if (attrs["action"] == ExternalPayment.Status.CONTESTED and
                len(attrs.get("reason", "").strip()) < 8):
            raise serializers.ValidationError(
                {"reason": "A contestação precisa de motivo (mínimo 8 caracteres)."}
            )
        return attrs


class ExternalPaymentEventReadSerializer(serializers.ModelSerializer):
    actor_user_id = serializers.IntegerField(source="actor_id", read_only=True)

    class Meta:
        model = ExternalPaymentEvent
        fields = ["id", "actor_user_id", "status_after", "note", "recorded_at"]
        read_only_fields = fields


class ExternalPaymentReadSerializer(serializers.ModelSerializer):
    reported_by_user_id = serializers.IntegerField(source="reported_by_id", read_only=True)
    responded_by_user_id = serializers.IntegerField(source="responded_by_id", read_only=True)
    history = ExternalPaymentEventReadSerializer(many=True, read_only=True)

    class Meta:
        model = ExternalPayment
        fields = [
            "id", "contract_id", "agreement_version_id", "agreement_condition_id",
            "amount", "method", "stage", "moment", "paid_on", "external_reference",
            "notes", "status", "reported_by_user_id", "responded_by_user_id",
            "response_note", "created_at", "updated_at", "history",
        ]
        read_only_fields = fields
