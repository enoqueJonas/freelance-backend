from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Opportunity",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=160)),
                ("description", models.TextField()),
                ("status", models.CharField(choices=[("DRAFT", "Draft"), ("OPEN", "Open"), ("CLOSED", "Closed")], default="DRAFT", max_length=12)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("employer", models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name="opportunities", to="accounts.employer")),
            ],
        ),
        migrations.CreateModel(
            name="Proposal",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("description", models.TextField()),
                ("status", models.CharField(choices=[("SUBMITTED", "Submitted"), ("ACCEPTED", "Accepted"), ("REJECTED", "Rejected")], default="SUBMITTED", max_length=12)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("opportunity", models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name="proposals", to="marketplace.opportunity")),
                ("worker", models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name="proposals", to="accounts.worker")),
            ],
            options={
                "constraints": [
                    models.UniqueConstraint(fields=("opportunity", "worker"), name="unique_worker_opportunity_proposal"),
                ],
            },
        ),
    ]
