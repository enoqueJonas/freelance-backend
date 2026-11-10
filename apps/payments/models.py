"""External payment declarations, never banking transactions or custody of funds."""
from django.conf import settings
from django.db import models


class ExternalPayment(models.Model):
    class Method(models.TextChoices):
        MPESA = "M-Pesa", "M-Pesa"
        EMOLA = "e-Mola", "e-Mola"
        BANK = "Transferência Bancária", "Transferência Bancária"
        OTHER = "Outro", "Outro"

    class Stage(models.TextChoices):
        ADVANCE = "ADVANCE", "Adiantamento"
        MILESTONE = "MILESTONE", "Etapa"
        FINAL = "FINAL", "Final"

    class Status(models.TextChoices):
        REPORTED_PAID = "REPORTED_PAID", "Declarado pelo empregador"
        CONFIRMED = "CONFIRMED", "Recepção declarada pelo trabalhador"
        CONTESTED = "CONTESTED", "Contestado pelo trabalhador"

    contract = models.ForeignKey(
        "contracts.Contract", on_delete=models.PROTECT,
        related_name="external_payments",
    )
    agreement_version = models.ForeignKey(
        "contracts.AgreementVersion", on_delete=models.PROTECT,
        related_name="external_payments",
    )
    agreement_condition_id = models.CharField(max_length=64)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    method = models.CharField(max_length=32, choices=Method.choices)
    stage = models.CharField(max_length=12, choices=Stage.choices)
    moment = models.CharField(max_length=300)
    paid_on = models.DateField()
    external_reference = models.CharField(max_length=200, blank=True)
    notes = models.TextField(blank=True)
    status = models.CharField(
        max_length=20, choices=Status.choices, default=Status.REPORTED_PAID,
    )
    reported_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT,
        related_name="payment_declarations",
    )
    responded_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT,
        related_name="payment_responses", null=True, blank=True,
    )
    response_note = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "conecta_external_payments"
        ordering = ["-created_at", "-id"]
        constraints = [
            models.CheckConstraint(
                condition=models.Q(amount__gt=0), name="external_payment_amount_positive"
            ),
        ]


class ExternalPaymentEvent(models.Model):
    payment = models.ForeignKey(
        ExternalPayment, on_delete=models.PROTECT, related_name="history",
    )
    actor = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT,
        related_name="external_payment_events",
    )
    status_after = models.CharField(
        max_length=20, choices=ExternalPayment.Status.choices,
    )
    note = models.TextField()
    recorded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "conecta_external_payment_events"
        ordering = ["recorded_at", "id"]
