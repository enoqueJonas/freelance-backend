# Initial persistent opportunity and proposal tables for ConecTA.
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Offer",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=180)),
                ("description", models.TextField()),
                ("category", models.CharField(max_length=100)),
                ("required_skills", models.JSONField(default=list)),
                ("budget", models.DecimalField(max_digits=12, decimal_places=2)),
                ("location", models.CharField(max_length=150)),
                ("status", models.CharField(
                    choices=[("active", "Active"), ("closed", "Closed")],
                    default="active", max_length=16,
                )),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("employer", models.ForeignKey(
                    on_delete=django.db.models.deletion.PROTECT,
                    related_name="offers",
                    to="accounts.employer",
                )),
            ],
            options={
                "db_table": "marketplace_offers",
                "ordering": ["-created_at", "-id"],
            },
        ),
        migrations.CreateModel(
            name="Proposal",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("description", models.TextField()),
                ("proposed_amount", models.DecimalField(max_digits=12, decimal_places=2)),
                ("timeline_days", models.PositiveIntegerField()),
                ("status", models.CharField(
                    choices=[("pending", "Pending"), ("accepted", "Accepted"), ("rejected", "Rejected")],
                    default="pending", max_length=16,
                )),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("offer", models.ForeignKey(
                    on_delete=django.db.models.deletion.PROTECT,
                    related_name="proposals",
                    to="marketplace.offer",
                )),
                ("worker", models.ForeignKey(
                    on_delete=django.db.models.deletion.PROTECT,
                    related_name="proposals",
                    to="accounts.worker",
                )),
            ],
            options={
                "db_table": "marketplace_proposals",
                "ordering": ["-created_at", "-id"],
            },
        ),
        migrations.AddConstraint(
            model_name="offer",
            constraint=models.CheckConstraint(
                condition=models.Q(budget__gt=0), name="offer_budget_positive"
            ),
        ),
        migrations.AddConstraint(
            model_name="proposal",
            constraint=models.UniqueConstraint(
                fields=("offer", "worker"), name="unique_worker_offer_proposal"
            ),
        ),
        migrations.AddConstraint(
            model_name="proposal",
            constraint=models.CheckConstraint(
                condition=models.Q(proposed_amount__gt=0),
                name="proposal_amount_positive",
            ),
        ),
        migrations.AddConstraint(
            model_name="proposal",
            constraint=models.CheckConstraint(
                condition=models.Q(timeline_days__gte=1),
                name="proposal_timeline_positive",
            ),
        ),
    ]
