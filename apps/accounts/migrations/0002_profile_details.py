"""Add optional public profile metadata without exposing contact or identity documents."""
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("accounts", "0001_initial")]

    operations = [
        migrations.AlterField(
            model_name="employer", name="address",
            field=models.CharField(blank=True, default="", max_length=150),
        ),
        migrations.AddField(
            model_name="employer", name="contact_name",
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name="employer", name="description",
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name="employer", name="industry",
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AddField(
            model_name="employer", name="location",
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name="employer", name="website_url",
            field=models.URLField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name="worker", name="title",
            field=models.CharField(blank=True, max_length=180),
        ),
        migrations.AddField(
            model_name="worker", name="bio",
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name="worker", name="location",
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name="worker", name="experience_years",
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="worker", name="github_url",
            field=models.URLField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name="worker", name="portfolio_url",
            field=models.URLField(blank=True, max_length=300),
        ),
    ]
