"""Input validation and read representations for marketplace entities."""
from rest_framework import serializers

from .models import Offer, Proposal


class OfferSerializer(serializers.ModelSerializer):
    employer_user_id = serializers.IntegerField(source="employer.user_id", read_only=True)
    employer_name = serializers.CharField(
        source="employer.company_name", read_only=True
    )
    required_skills = serializers.ListField(
        child=serializers.CharField(max_length=60, allow_blank=False),
        allow_empty=True,
        max_length=20,
    )

    class Meta:
        model = Offer
        fields = [
            "id", "employer_user_id", "employer_name", "title",
            "description", "category", "required_skills", "budget",
            "location", "status", "created_at", "updated_at",
        ]
        read_only_fields = [
            "id", "employer_user_id", "employer_name", "status",
            "created_at", "updated_at",
        ]

    def validate_title(self, value):
        if len(value.strip()) < 5:
            raise serializers.ValidationError("O título é demasiado curto.")
        return value.strip()

    def validate_description(self, value):
        if len(value.strip()) < 20:
            raise serializers.ValidationError("Descreva claramente a oportunidade.")
        return value.strip()

    def validate_required_skills(self, value):
        cleaned = [part.strip() for part in value]
        if len(set(part.casefold() for part in cleaned)) != len(cleaned):
            raise serializers.ValidationError("Competências duplicadas.")
        return cleaned

    def validate_budget(self, value):
        if value <= 0:
            raise serializers.ValidationError("O valor deve ser positivo.")
        return value


class ProposalSerializer(serializers.ModelSerializer):
    offer_id = serializers.IntegerField(read_only=True)
    worker_user_id = serializers.IntegerField(source="worker.user_id", read_only=True)
    worker_name = serializers.CharField(source="worker.user.name", read_only=True)

    class Meta:
        model = Proposal
        fields = [
            "id", "offer_id", "worker_user_id", "worker_name",
            "description", "proposed_amount", "timeline_days",
            "status", "created_at",
        ]
        read_only_fields = fields


class ProposalCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proposal
        fields = ["description", "proposed_amount", "timeline_days"]

    def validate_description(self, value):
        description = value.strip()
        if len(description) < 15:
            raise serializers.ValidationError("Explique a sua proposta.")
        return description

    def validate_proposed_amount(self, value):
        if value <= 0:
            raise serializers.ValidationError("O valor deve ser positivo.")
        return value

    def validate_timeline_days(self, value):
        if value < 1 or value > 365:
            raise serializers.ValidationError("O prazo deve estar entre 1 e 365 dias.")
        return value
