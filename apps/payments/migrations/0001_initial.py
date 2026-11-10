import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("contracts", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="ExternalPayment",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("agreement_condition_id", models.CharField(max_length=64)),
                ("amount", models.DecimalField(max_digits=12, decimal_places=2)),
                ("method", models.CharField(max_length=32, choices=[
                    ("M-Pesa", "M-Pesa"), ("e-Mola", "e-Mola"),
                    ("Transferência Bancária", "Transferência Bancária"), ("Outro", "Outro"),
                ])),
                ("stage", models.CharField(max_length=12, choices=[
                    ("ADVANCE", "Adiantamento"), ("MILESTONE", "Etapa"), ("FINAL", "Final"),
                ])),
                ("moment", models.CharField(max_length=300)),
                ("paid_on", models.DateField()),
                ("external_reference", models.CharField(max_length=200, blank=True)),
                ("notes", models.TextField(blank=True)),
                ("status", models.CharField(max_length=20, choices=[
                    ("REPORTED_PAID", "Declarado pelo empregador"),
                    ("CONFIRMED", "Recepção declarada pelo trabalhador"),
                    ("CONTESTED", "Contestado pelo trabalhador"),
                ], default="REPORTED_PAID")),
                ("response_note", models.TextField(blank=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("agreement_version", models.ForeignKey(
                    on_delete=django.db.models.deletion.PROTECT,
                    related_name="external_payments", to="contracts.agreementversion",
                )),
                ("contract", models.ForeignKey(
                    on_delete=django.db.models.deletion.PROTECT,
                    related_name="external_payments", to="contracts.contract",
                )),
                ("reported_by", models.ForeignKey(
                    on_delete=django.db.models.deletion.PROTECT,
                    related_name="payment_declarations", to=settings.AUTH_USER_MODEL,
                )),
                ("responded_by", models.ForeignKey(
                    null=True, blank=True, on_delete=django.db.models.deletion.PROTECT,
                    related_name="payment_responses", to=settings.AUTH_USER_MODEL,
                )),
            ],
            options={
                "db_table": "conecta_external_payments",
                "ordering": ["-created_at", "-id"],
            },
        ),
        migrations.CreateModel(
            name="ExternalPaymentEvent",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("status_after", models.CharField(max_length=20, choices=[
                    ("REPORTED_PAID", "Declarado pelo empregador"),
                    ("CONFIRMED", "Recepção declarada pelo trabalhador"),
                    ("CONTESTED", "Contestado pelo trabalhador"),
                ])),
                ("note", models.TextField()),
                ("recorded_at", models.DateTimeField(auto_now_add=True)),
                ("actor", models.ForeignKey(
                    on_delete=django.db.models.deletion.PROTECT,
                    related_name="external_payment_events", to=settings.AUTH_USER_MODEL,
                )),
                ("payment", models.ForeignKey(
                    on_delete=django.db.models.deletion.PROTECT,
                    related_name="history", to="payments.externalpayment",
                )),
            ],
            options={
                "db_table": "conecta_external_payment_events",
                "ordering": ["recorded_at", "id"],
            },
        ),
        migrations.AddConstraint(
            model_name="externalpayment",
            constraint=models.CheckConstraint(
                condition=models.Q(amount__gt=0), name="external_payment_amount_positive",
            ),
        ),
    ]
