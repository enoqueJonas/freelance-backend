from django.conf import settings
from django.db import models


class Opportunity(models.Model):
    class Status(models.TextChoices):
        DRAFT = "DRAFT", "Draft"
        OPEN = "OPEN", "Open"
        CLOSED = "CLOSED", "Closed"

    employer = models.ForeignKey(
        "accounts.Employer", on_delete=models.PROTECT, related_name="opportunities"
    )
    title = models.CharField(max_length=160)
    description = models.TextField()
    status = models.CharField(
        max_length=12, choices=Status.choices, default=Status.DRAFT
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Proposal(models.Model):
    class Status(models.TextChoices):
        SUBMITTED = "SUBMITTED", "Submitted"
        ACCEPTED = "ACCEPTED", "Accepted"
        REJECTED = "REJECTED", "Rejected"

    opportunity = models.ForeignKey(
        Opportunity, on_delete=models.PROTECT, related_name="proposals"
    )
    worker = models.ForeignKey(
        "accounts.Worker", on_delete=models.PROTECT, related_name="proposals"
    )
    description = models.TextField()
    status = models.CharField(
        max_length=12, choices=Status.choices, default=Status.SUBMITTED
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["opportunity", "worker"],
                name="unique_worker_opportunity_proposal",
            ),
        ]

    def __str__(self):
        return f"{self.opportunity_id}: {self.worker_id}"
