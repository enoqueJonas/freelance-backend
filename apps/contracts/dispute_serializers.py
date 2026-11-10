"""Dispute input fields and read-only audit history; no certified evidence."""
from rest_framework import serializers
from .models import Dispute, DisputeEvidence, DisputeEvent


def https_or_http(value):
    if value and not value.lower().startswith(("http://", "https://")):
        raise serializers.ValidationError("A referência tem de ser HTTP(S).")
    return value


class DisputeReportSerializer(serializers.Serializer):
    contract_id = serializers.IntegerField(min_value=1)
    category = serializers.ChoiceField(choices=Dispute.Category.choices)
    description = serializers.CharField(min_length=20, max_length=4000)
    evidence_description = serializers.CharField(min_length=8, max_length=2000)
    evidence_url = serializers.URLField(
        max_length=400, allow_blank=True, required=False, validators=[https_or_http]
    )


class DisputeEvidenceInputSerializer(serializers.Serializer):
    description = serializers.CharField(min_length=8, max_length=2000)
    url = serializers.URLField(
        max_length=400, allow_blank=True, required=False, validators=[https_or_http]
    )


class DisputeNoteSerializer(serializers.Serializer):
    note = serializers.CharField(min_length=8, max_length=4000)


class DisputeQuestionSerializer(serializers.Serializer):
    requested_from_user_id = serializers.IntegerField(min_value=1)
    note = serializers.CharField(min_length=12, max_length=4000)


class DisputeResultSerializer(serializers.Serializer):
    note = serializers.CharField(min_length=20, max_length=4000)


class DisputeEvidenceReadSerializer(serializers.ModelSerializer):
    author_user_id = serializers.IntegerField(source="author_id", read_only=True)

    class Meta:
        model = DisputeEvidence
        fields = ["id", "author_user_id", "description", "url", "created_at"]
        read_only_fields = fields


class DisputeEventReadSerializer(serializers.ModelSerializer):
    actor_user_id = serializers.IntegerField(source="actor_id", read_only=True)

    class Meta:
        model = DisputeEvent
        fields = [
            "id", "actor_user_id", "action", "status_after", "note", "recorded_at",
        ]
        read_only_fields = fields


class DisputeReadSerializer(serializers.ModelSerializer):
    reported_by_user_id = serializers.IntegerField(source="reported_by_id", read_only=True)
    requested_from_user_id = serializers.IntegerField(source="requested_from_id", read_only=True)
    employer_user_id = serializers.IntegerField(
        source="contract.employer.user_id", read_only=True
    )
    worker_user_id = serializers.IntegerField(
        source="contract.worker.user_id", read_only=True
    )
    evidence = DisputeEvidenceReadSerializer(many=True, read_only=True)
    events = DisputeEventReadSerializer(many=True, read_only=True)

    class Meta:
        model = Dispute
        fields = [
            "id", "contract_id", "employer_user_id", "worker_user_id",
            "reported_by_user_id", "category", "description", "status",
            "requested_from_user_id", "administrative_result",
            "created_at", "updated_at", "evidence", "events",
        ]
        read_only_fields = fields
