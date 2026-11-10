"""Real marketplace persistence; the earlier models/ directory contains only stubs."""
from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models


class Offer(models.Model):
    class Status(models.TextChoices):
        ACTIVE = "active", "Active"
        CLOSED = "closed", "Closed"

    employer = models.ForeignKey(
        "accounts.Employer", on_delete=models.PROTECT,
        related_name="offers",
    )
    title = models.CharField(max_length=180)
    description = models.TextField()
    category = models.CharField(max_length=100)
    required_skills = models.JSONField(default=list)
    budget = models.DecimalField(max_digits=12, decimal_places=2)
    location = models.CharField(max_length=150)
    status = models.CharField(
        max_length=16, choices=Status.choices, default=Status.ACTIVE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "marketplace_offers"
        ordering = ["-created_at", "-id"]
        constraints = [
            models.CheckConstraint(
                condition=models.Q(budget__gt=0),
                name="offer_budget_positive",
            ),
        ]

    def __str__(self):
        return self.title


class Proposal(models.Model):
    class Status(models.TextChoices):
        PENDING = "pending", "Pending"
        ACCEPTED = "accepted", "Accepted"
        REJECTED = "rejected", "Rejected"

    offer = models.ForeignKey(
        Offer, on_delete=models.PROTECT, related_name="proposals"
    )
    worker = models.ForeignKey(
        "accounts.Worker", on_delete=models.PROTECT, related_name="proposals"
    )
    description = models.TextField()
    proposed_amount = models.DecimalField(max_digits=12, decimal_places=2)
    timeline_days = models.PositiveIntegerField()
    status = models.CharField(
        max_length=16, choices=Status.choices, default=Status.PENDING
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "marketplace_proposals"
        ordering = ["-created_at", "-id"]
        constraints = [
            models.UniqueConstraint(
                fields=["offer", "worker"], name="unique_worker_offer_proposal"
            ),
            models.CheckConstraint(
                condition=models.Q(proposed_amount__gt=0),
                name="proposal_amount_positive",
            ),
            models.CheckConstraint(
                condition=models.Q(timeline_days__gte=1),
                name="proposal_timeline_positive",
            ),
        ]

    def clean(self):
        super().clean()
        if self.offer_id and self.worker_id:
            if self.offer.employer.user_id == self.worker.user_id:
                raise ValidationError(
                    "Uma conta não pode candidatar-se à sua própria oportunidade."
                )

    def __str__(self):
        return f"Proposal {self.pk} for offer {self.offer_id}"
