import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("contracts", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Dispute",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("category", models.CharField(max_length=16, choices=[
                    ("SCOPE", "Âmbito"), ("DEADLINE", "Prazo"), ("DELIVERABLE", "Entregáveis"),
                    ("PAYMENT", "Pagamento"), ("COMMUNICATION", "Comunicação"), ("OTHER", "Outro"),
                ])),
                ("description", models.TextField()),
                ("status", models.CharField(max_length=24, default="OPEN", choices=[
                    ("OPEN", "Reportado"), ("UNDER_REVIEW", "Em análise"),
                    ("WAITING_INFORMATION", "A aguardar informação"),
                    ("RESOLVED", "Resultado administrativo registado"),
                    ("CLOSED", "Acompanhamento encerrado"),
                ])),
                ("administrative_result", models.TextField(blank=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("contract", models.ForeignKey(
                    on_delete=django.db.models.deletion.PROTECT,
                    related_name="disputes", to="contracts.contract",
                )),
                ("reported_by", models.ForeignKey(
                    on_delete=django.db.models.deletion.PROTECT,
                    related_name="reported_disputes", to=settings.AUTH_USER_MODEL,
                )),
                ("requested_from", models.ForeignKey(
                    null=True, blank=True, on_delete=django.db.models.deletion.PROTECT,
                    related_name="dispute_information_requests", to=settings.AUTH_USER_MODEL,
                )),
            ],
            options={"db_table": "conecta_disputes", "ordering": ["-created_at", "-id"]},
        ),
        migrations.CreateModel(
            name="DisputeEvidence",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("description", models.TextField()),
                ("url", models.URLField(max_length=400, blank=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("author", models.ForeignKey(
                    on_delete=django.db.models.deletion.PROTECT,
                    related_name="submitted_dispute_evidence", to=settings.AUTH_USER_MODEL,
                )),
                ("dispute", models.ForeignKey(
                    on_delete=django.db.models.deletion.PROTECT,
                    related_name="evidence", to="contracts.dispute",
                )),
            ],
            options={"db_table": "conecta_dispute_evidence", "ordering": ["created_at", "id"]},
        ),
        migrations.CreateModel(
            name="DisputeEvent",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("action", models.CharField(max_length=32)),
                ("status_after", models.CharField(max_length=24, choices=[
                    ("OPEN", "Reportado"), ("UNDER_REVIEW", "Em análise"),
                    ("WAITING_INFORMATION", "A aguardar informação"),
                    ("RESOLVED", "Resultado administrativo registado"),
                    ("CLOSED", "Acompanhamento encerrado"),
                ])),
                ("note", models.TextField()),
                ("recorded_at", models.DateTimeField(auto_now_add=True)),
                ("actor", models.ForeignKey(
                    on_delete=django.db.models.deletion.PROTECT,
                    related_name="dispute_events", to=settings.AUTH_USER_MODEL,
                )),
                ("dispute", models.ForeignKey(
                    on_delete=django.db.models.deletion.PROTECT,
                    related_name="events", to="contracts.dispute",
                )),
            ],
            options={"db_table": "conecta_dispute_events", "ordering": ["recorded_at", "id"]},
        ),
    ]
