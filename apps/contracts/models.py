"""Contract and agreement-version models (RF13/RF14).

These are server-owned records. Client requests can edit only draft *terms*,
never approvals, participant IDs, status, or the event history.
"""
from django.conf import settings
from django.db import models


class Contract(models.Model):
    class Status(models.TextChoices):
        PENDING = "pending", "Pending bilateral agreement"
        ACTIVE = "active", "Active"
        COMPLETED = "completed", "Completed"

    offer = models.OneToOneField(
        "marketplace.Offer", on_delete=models.PROTECT,
        related_name="contract",
    )
    proposal = models.OneToOneField(
        "marketplace.Proposal", on_delete=models.PROTECT,
        related_name="contract",
    )
    employer = models.ForeignKey(
        "accounts.Employer", on_delete=models.PROTECT,
        related_name="contracts",
    )
    worker = models.ForeignKey(
        "accounts.Worker", on_delete=models.PROTECT,
        related_name="contracts",
    )
    title = models.CharField(max_length=180)
    scope = models.TextField()
    budget = models.DecimalField(max_digits=12, decimal_places=2)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    status = models.CharField(
        max_length=16, choices=Status.choices, default=Status.PENDING
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "conecta_contracts"
        ordering = ["-created_at", "-id"]
        constraints = [
            models.CheckConstraint(
                condition=models.Q(budget__gt=0),
                name="contract_budget_positive",
            ),
        ]

    def __str__(self):
        return f"Contract {self.pk}: {self.title}"


class AgreementVersion(models.Model):
    class Status(models.TextChoices):
        DRAFT = "draft", "Draft"
        PENDING_APPROVAL = "pending_approval", "Pending approval"
        ACTIVE = "active", "Active"
        SUPERSEDED = "superseded", "Superseded"
        REJECTED = "rejected", "Rejected"

    contract = models.ForeignKey(
        Contract, on_delete=models.PROTECT, related_name="agreement_versions"
    )
    number = models.PositiveIntegerField()
    status = models.CharField(
        max_length=20, choices=Status.choices, default=Status.DRAFT
    )
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT,
        related_name="authored_agreement_versions",
    )
    reason = models.TextField()
    terms = models.JSONField(default=dict)
    submitted_at = models.DateTimeField(null=True, blank=True)
    rejected_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT,
        related_name="rejected_agreement_versions",
        null=True, blank=True,
    )
    rejection_reason = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "conecta_agreement_versions"
        ordering = ["-number"]
        constraints = [
            models.UniqueConstraint(
                fields=["contract", "number"], name="agreement_unique_number"
            ),
            models.UniqueConstraint(
                fields=["contract"],
                condition=models.Q(status="active"),
                name="agreement_one_active_per_contract",
            ),
            models.UniqueConstraint(
                fields=["contract"],
                condition=models.Q(status__in=["draft", "pending_approval"]),
                name="agreement_one_open_per_contract",
            ),
        ]

    def __str__(self):
        return f"Contract {self.contract_id} v{self.number} ({self.status})"


class AgreementApproval(models.Model):
    class Party(models.TextChoices):
        EMPLOYER = "employer", "Employer"
        WORKER = "worker", "Worker"

    version = models.ForeignKey(
        AgreementVersion, on_delete=models.PROTECT,
        related_name="approvals",
    )
    party = models.CharField(max_length=10, choices=Party.choices)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT,
        related_name="agreement_approvals",
    )
    approved_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "conecta_agreement_approvals"
        constraints = [
            models.UniqueConstraint(
                fields=["version", "party"], name="agreement_one_approval_per_party"
            ),
        ]


class AgreementEvent(models.Model):
    version = models.ForeignKey(
        AgreementVersion, on_delete=models.PROTECT,
        related_name="events",
    )
    actor = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT,
        related_name="agreement_events",
    )
    action = models.CharField(max_length=32)
    status_after = models.CharField(max_length=20)
    note = models.TextField()
    recorded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "conecta_agreement_events"
        ordering = ["recorded_at", "id"]
