from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("marketplace", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Engagement",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("status", models.CharField(choices=[("PENDING_AGREEMENT", "Pending agreement"), ("ACTIVE", "Active")], default="PENDING_AGREEMENT", max_length=20)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("proposal", models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name="engagement", to="marketplace.proposal")),
            ],
        ),
        migrations.CreateModel(
            name="AgreementVersion",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("version", models.PositiveIntegerField()),
                ("scope", models.TextField()),
                ("amount", models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ("price_after_diagnosis", models.BooleanField(default=False)),
                ("content_fingerprint", models.CharField(max_length=64)),
                ("status", models.CharField(choices=[("PROPOSED", "Proposed"), ("ACCEPTED", "Accepted")], default="PROPOSED", max_length=10)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("engagement", models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name="agreement_versions", to="contracts.engagement")),
                ("proposed_by", models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name="proposed_agreement_versions", to=settings.AUTH_USER_MODEL)),
            ],
            options={
                "constraints": [
                    models.UniqueConstraint(fields=("engagement", "version"), name="unique_engagement_agreement_version"),
                ],
            },
        ),
        migrations.CreateModel(
            name="AgreementAcceptance",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("content_fingerprint", models.CharField(max_length=64)),
                ("accepted_at", models.DateTimeField(auto_now_add=True)),
                ("actor", models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name="agreement_acceptances", to=settings.AUTH_USER_MODEL)),
                ("agreement_version", models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name="acceptances", to="contracts.agreementversion")),
            ],
            options={
                "constraints": [
                    models.UniqueConstraint(fields=("agreement_version", "actor"), name="unique_agreement_version_actor_acceptance"),
                ],
            },
        ),
    ]
