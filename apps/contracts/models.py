from django.conf import settings
from django.db import models


class Engagement(models.Model):
    class Status(models.TextChoices):
        PENDING_AGREEMENT = "PENDING_AGREEMENT", "Pending agreement"
        ACTIVE = "ACTIVE", "Active"

    proposal = models.OneToOneField(
        "marketplace.Proposal", on_delete=models.PROTECT, related_name="engagement"
    )
    status = models.CharField(
        max_length=20, choices=Status.choices, default=Status.PENDING_AGREEMENT
    )
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def worker_user_id(self):
        return self.proposal.worker.user_id

    @property
    def employer_user_id(self):
        return self.proposal.opportunity.employer.user_id


class AgreementVersion(models.Model):
    class Status(models.TextChoices):
        PROPOSED = "PROPOSED", "Proposed"
        ACCEPTED = "ACCEPTED", "Accepted"

    engagement = models.ForeignKey(
        Engagement, on_delete=models.PROTECT, related_name="agreement_versions"
    )
    version = models.PositiveIntegerField()
    scope = models.TextField()
    amount = models.DecimalField(
        max_digits=12, decimal_places=2, null=True, blank=True
    )
    price_after_diagnosis = models.BooleanField(default=False)
    content_fingerprint = models.CharField(max_length=64)
    status = models.CharField(
        max_length=10, choices=Status.choices, default=Status.PROPOSED
    )
    proposed_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT,
        related_name="proposed_agreement_versions"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["engagement", "version"],
                name="unique_engagement_agreement_version"
            ),
        ]


class AgreementAcceptance(models.Model):
    agreement_version = models.ForeignKey(
        AgreementVersion, on_delete=models.PROTECT, related_name="acceptances"
    )
    actor = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT,
        related_name="agreement_acceptances"
    )
    content_fingerprint = models.CharField(max_length=64)
    accepted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["agreement_version", "actor"],
                name="unique_agreement_version_actor_acceptance",
            ),
        ]
