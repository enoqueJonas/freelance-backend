"""Minimal evidence-reference review (RN03/RN15/RF05/RF06).

No identity-document storage, financial KYC, automated authenticity checks,
certified signatures, or guarantee of the claimed qualifications.
"""
from django.conf import settings
from django.db import models


class ProfileEvidenceReview(models.Model):
    class Kind(models.TextChoices):
        PORTFOLIO = "PORTFOLIO", "Portefólio profissional"
        CERTIFICATE = "CERTIFICATE", "Certificação declarada"
        BUSINESS_REFERENCE = "BUSINESS_REFERENCE", "Referência da organização"

    class Status(models.TextChoices):
        PENDING = "PENDING", "Por analisar"
        REVIEWED = "REVIEWED", "Referência analisada"
        REJECTED = "REJECTED", "Referência rejeitada"

    worker = models.ForeignKey(
        "accounts.Worker", null=True, blank=True,
        on_delete=models.PROTECT, related_name="evidence_reviews",
    )
    employer = models.ForeignKey(
        "accounts.Employer", null=True, blank=True,
        on_delete=models.PROTECT, related_name="evidence_reviews",
    )
    submitted_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT,
        related_name="submitted_evidence_reviews",
    )
    kind = models.CharField(max_length=24, choices=Kind.choices)
    description = models.TextField()
    reference_url = models.URLField(max_length=400)
    status = models.CharField(
        max_length=12, choices=Status.choices, default=Status.PENDING,
    )
    reviewed_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True, blank=True,
        on_delete=models.PROTECT, related_name="handled_evidence_reviews",
    )
    review_note = models.TextField(blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
    reviewed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = "conecta_profile_evidence_reviews"
        ordering = ["-submitted_at", "-id"]
        constraints = [
            models.CheckConstraint(
                condition=(
                    (models.Q(worker__isnull=False) & models.Q(employer__isnull=True))
                    | (models.Q(worker__isnull=True) & models.Q(employer__isnull=False))
                ),
                name="evidence_exactly_one_profile",
            ),
            models.UniqueConstraint(
                fields=["worker"],
                condition=models.Q(status="PENDING", worker__isnull=False),
                name="evidence_one_pending_per_worker",
            ),
            models.UniqueConstraint(
                fields=["employer"],
                condition=models.Q(status="PENDING", employer__isnull=False),
                name="evidence_one_pending_per_employer",
            ),
        ]

    def __str__(self):
        target = f"worker={self.worker_id}" if self.worker_id else f"employer={self.employer_id}"
        return f"Evidence {self.pk}: {target} ({self.status})"
