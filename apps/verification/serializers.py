"""Private reference-review payloads; no uploads, BI, NUIT or KYC."""
from rest_framework import serializers

from apps.accounts.serializers import public_https_url
from .models import ProfileEvidenceReview


class EvidenceSubmissionSerializer(serializers.Serializer):
    profile_role = serializers.ChoiceField(choices=("worker", "employer"))
    kind = serializers.ChoiceField(choices=ProfileEvidenceReview.Kind.choices)
    description = serializers.CharField(min_length=20, max_length=2000)
    reference_url = serializers.URLField(max_length=400)

    def validate_reference_url(self, value):
        return public_https_url(value)

    def validate(self, attrs):
        allowed = {
            "worker": {
                ProfileEvidenceReview.Kind.PORTFOLIO,
                ProfileEvidenceReview.Kind.CERTIFICATE,
            },
            "employer": {ProfileEvidenceReview.Kind.BUSINESS_REFERENCE},
        }
        if attrs["kind"] not in allowed[attrs["profile_role"]]:
            raise serializers.ValidationError({
                "kind": "Tipo de referência incompatível com o perfil."
            })
        attrs["description"] = attrs["description"].strip()
        return attrs


class EvidenceDecisionSerializer(serializers.Serializer):
    decision = serializers.ChoiceField(choices=(
        ProfileEvidenceReview.Status.REVIEWED,
        ProfileEvidenceReview.Status.REJECTED,
    ))
    note = serializers.CharField(min_length=12, max_length=1000)

    def validate_note(self, value):
        return value.strip()


class EvidenceReviewReadSerializer(serializers.ModelSerializer):
    submitted_by_user_id = serializers.IntegerField(source="submitted_by_id", read_only=True)
    reviewed_by_user_id = serializers.IntegerField(source="reviewed_by_id", read_only=True)
    profile_role = serializers.SerializerMethodField()

    class Meta:
        model = ProfileEvidenceReview
        fields = [
            "id", "profile_role", "worker_id", "employer_id",
            "kind", "description", "reference_url", "status",
            "submitted_by_user_id", "submitted_at",
            "reviewed_by_user_id", "reviewed_at", "review_note",
        ]
        read_only_fields = fields

    def get_profile_role(self, obj):
        return "worker" if obj.worker_id is not None else "employer"
