# Initial contracts and bilateral agreement-version history.
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("marketplace", "0001_initial"),
        ("accounts", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Contract",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=180)),
                ("scope", models.TextField()),
                ("budget", models.DecimalField(max_digits=12, decimal_places=2)),
                ("start_date", models.DateField(blank=True, null=True)),
                ("end_date", models.DateField(blank=True, null=True)),
                ("status", models.CharField(
                    choices=[("pending", "Pending bilateral agreement"),
                             ("active", "Active"), ("completed", "Completed")],
                    default="pending", max_length=16,
                )),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("employer", models.ForeignKey(
                    on_delete=django.db.models.deletion.PROTECT,
                    related_name="contracts", to="accounts.employer",
                )),
                ("worker", models.ForeignKey(
                    on_delete=django.db.models.deletion.PROTECT,
                    related_name="contracts", to="accounts.worker",
                )),
                ("offer", models.OneToOneField(
                    on_delete=django.db.models.deletion.PROTECT,
                    related_name="contract", to="marketplace.offer",
                )),
                ("proposal", models.OneToOneField(
                    on_delete=django.db.models.deletion.PROTECT,
                    related_name="contract", to="marketplace.proposal",
                )),
            ],
            options={
                "db_table": "conecta_contracts",
                "ordering": ["-created_at", "-id"],
            },
        ),
        migrations.CreateModel(
            name="AgreementVersion",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("number", models.PositiveIntegerField()),
                ("status", models.CharField(
                    choices=[("draft", "Draft"), ("pending_approval", "Pending approval"),
                             ("active", "Active"), ("superseded", "Superseded"), ("rejected", "Rejected")],
                    default="draft", max_length=20,
                )),
                ("reason", models.TextField()),
                ("terms", models.JSONField(default=dict)),
                ("submitted_at", models.DateTimeField(blank=True, null=True)),
                ("rejection_reason", models.TextField(blank=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("contract", models.ForeignKey(
                    on_delete=django.db.models.deletion.PROTECT,
                    related_name="agreement_versions", to="contracts.contract",
                )),
                ("created_by", models.ForeignKey(
                    on_delete=django.db.models.deletion.PROTECT,
                    related_name="authored_agreement_versions", to=settings.AUTH_USER_MODEL,
                )),
                ("rejected_by", models.ForeignKey(
                    blank=True, null=True, on_delete=django.db.models.deletion.PROTECT,
                    related_name="rejected_agreement_versions", to=settings.AUTH_USER_MODEL,
                )),
            ],
            options={
                "db_table": "conecta_agreement_versions",
                "ordering": ["-number"],
            },
        ),
        migrations.CreateModel(
            name="AgreementApproval",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("party", models.CharField(
                    choices=[("employer", "Employer"), ("worker", "Worker")], max_length=10,
                )),
                ("approved_at", models.DateTimeField(auto_now_add=True)),
                ("user", models.ForeignKey(
                    on_delete=django.db.models.deletion.PROTECT,
                    related_name="agreement_approvals", to=settings.AUTH_USER_MODEL,
                )),
                ("version", models.ForeignKey(
                    on_delete=django.db.models.deletion.PROTECT,
                    related_name="approvals", to="contracts.agreementversion",
                )),
            ],
            options={"db_table": "conecta_agreement_approvals"},
        ),
        migrations.CreateModel(
            name="AgreementEvent",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("action", models.CharField(max_length=32)),
                ("status_after", models.CharField(max_length=20)),
                ("note", models.TextField()),
                ("recorded_at", models.DateTimeField(auto_now_add=True)),
                ("actor", models.ForeignKey(
                    on_delete=django.db.models.deletion.PROTECT,
                    related_name="agreement_events", to=settings.AUTH_USER_MODEL,
                )),
                ("version", models.ForeignKey(
                    on_delete=django.db.models.deletion.PROTECT,
                    related_name="events", to="contracts.agreementversion",
                )),
            ],
            options={
                "db_table": "conecta_agreement_events",
                "ordering": ["recorded_at", "id"],
            },
        ),
        migrations.AddConstraint(
            model_name="contract",
            constraint=models.CheckConstraint(
                condition=models.Q(budget__gt=0), name="contract_budget_positive",
            ),
        ),
        migrations.AddConstraint(
            model_name="agreementversion",
            constraint=models.UniqueConstraint(
                fields=("contract", "number"), name="agreement_unique_number",
            ),
        ),
        migrations.AddConstraint(
            model_name="agreementversion",
            constraint=models.UniqueConstraint(
                fields=("contract"), condition=models.Q(status="active"),
                name="agreement_one_active_per_contract",
            ),
        ),
        migrations.AddConstraint(
            model_name="agreementversion",
            constraint=models.UniqueConstraint(
                fields=("contract"), condition=models.Q(status__in=["draft", "pending_approval"]),
                name="agreement_one_open_per_contract",
            ),
        ),
        migrations.AddConstraint(
            model_name="agreementapproval",
            constraint=models.UniqueConstraint(
                fields=("version", "party"), name="agreement_one_approval_per_party",
            ),
        ),
    ]
