from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("contracts", "0001_initial"),
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
