from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("contracts", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name="agreementversion",
            name="status",
            field=models.CharField(
                max_length=10,
                default="PROPOSED",
                choices=[
                    ("PROPOSED", "Proposed"),
                    ("ACCEPTED", "Accepted"),
                    ("REJECTED", "Rejected"),
                    ("SUPERSEDED", "Superseded"),
                ],
            ),
        ),
        migrations.AddField(
            model_name="agreementversion",
            name="rejected_by",
            field=models.ForeignKey(
                to=settings.AUTH_USER_MODEL,
                related_name="rejected_agreement_versions",
                on_delete=django.db.models.deletion.PROTECT,
                null=True,
                blank=True,
            ),
        ),
        migrations.AddField(
            model_name="agreementversion",
            name="rejected_at",
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name="agreementversion",
            name="rejection_reason",
            field=models.TextField(blank=True, default=""),
        ),
        migrations.AddConstraint(
            model_name="agreementversion",
            constraint=models.UniqueConstraint(
                fields=("engagement",),
                condition=models.Q(status="PROPOSED"),
                name="one_proposed_agreement_per_engagement",
            ),
        ),
        migrations.AddConstraint(
            model_name="agreementversion",
            constraint=models.UniqueConstraint(
                fields=("engagement",),
                condition=models.Q(status="ACCEPTED"),
                name="one_current_agreement_per_engagement",
            ),
        ),
    ]
