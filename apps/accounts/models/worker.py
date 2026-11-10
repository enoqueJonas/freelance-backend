from django.db import models


class Worker(models.Model):
    """Public professional profile. Identity evidence is handled separately."""

    user = models.OneToOneField("accounts.User", on_delete=models.CASCADE)
    # Legacy compatibility: existing values are comma-separated strings.
    skills = models.CharField(max_length=200)
    experience = models.CharField(max_length=200, blank=True, default="")
    title = models.CharField(max_length=180, blank=True)
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=150, blank=True)
    experience_years = models.PositiveSmallIntegerField(null=True, blank=True)
    github_url = models.URLField(max_length=300, blank=True)
    portfolio_url = models.URLField(max_length=300, blank=True)

    class Meta:
        db_table = "workers"

    def __str__(self):
        return self.user.username
