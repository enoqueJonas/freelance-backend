"""Evidence-review metadata without identity scans or financial KYC."""
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("accounts", "0002_profile_details"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="ProfileEvidenceReview",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("kind", models.CharField(
                    max_length=24, choices=[
                        ("PORTFOLIO", "Portefólio profissional"),
                        ("CERTIFICATE", "Certificação declarada"),
                        ("BUSINESS_REFERENCE", "Referência da organização"),
                    ],
                )),
                ("description", models.TextField()),
                ("reference_url", models.URLField(max_length=400)),
                ("status", models.CharField(
                    max_length=12, default="PENDING",
                    choices=[
                        ("PENDING", "Por analisar"),
                        ("REVIEWED", "Referência analisada"),
                        ("REJECTED", "Referência rejeitada"),
                    ],
                )),
                ("review_note", models.TextField(blank=True)),
                ("submitted_at", models.DateTimeField(auto_now_add=True)),
                ("reviewed_at", models.DateTimeField(blank=True, null=True)),
                ("worker", models.ForeignKey(
                    blank=True, null=True, on_delete=django.db.models.deletion.PROTECT,
                    related_name="evidence_reviews", to="accounts.worker",
                )),
                ("employer", models.ForeignKey(
                    blank=True, null=True, on_delete=django.db.models.deletion.PROTECT,
                    related_name="evidence_reviews", to="accounts.employer",
                )),
                ("submitted_by", models.ForeignKey(
                    on_delete=django.db.models.deletion.PROTECT,
                    related_name="submitted_evidence_reviews", to=settings.AUTH_USER_MODEL,
                )),
                ("reviewed_by", models.ForeignKey(
                    blank=True, null=True, on_delete=django.db.models.deletion.PROTECT,
                    related_name="handled_evidence_reviews", to=settings.AUTH_USER_MODEL,
                )),
            ],
            options={
                "db_table": "conecta_profile_evidence_reviews",
                "ordering": ["-submitted_at", "-id"],
            },
        ),
        migrations.AddConstraint(
            model_name="profileevidencereview",
            constraint=models.CheckConstraint(
                condition=(
                    (models.Q(worker__isnull=False) & models.Q(employer__isnull=True))
                    | (models.Q(worker__isnull=True) & models.Q(employer__isnull=False))
                ),
                name="evidence_exactly_one_profile",
            ),
        ),
        migrations.AddConstraint(
            model_name="profileevidencereview",
            constraint=models.UniqueConstraint(
                fields=("worker",),
                condition=models.Q(status="PENDING", worker__isnull=False),
                name="evidence_one_pending_per_worker",
            ),
        ),
        migrations.AddConstraint(
            model_name="profileevidencereview",
            constraint=models.UniqueConstraint(
                fields=("employer",),
                condition=models.Q(status="PENDING", employer__isnull=False),
                name="evidence_one_pending_per_employer",
            ),
        ),
    ]
