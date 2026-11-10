from django.db import models


class Employer(models.Model):
    """A business profile independent from a user's professional profile."""

    user = models.OneToOneField("accounts.User", on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    # Location is contextual (RN04): a street address is never compulsory.
    address = models.CharField(max_length=150, blank=True, default="")
    contact_name = models.CharField(max_length=150, blank=True)
    description = models.TextField(blank=True)
    industry = models.CharField(max_length=120, blank=True)
    location = models.CharField(max_length=150, blank=True)
    website_url = models.URLField(max_length=300, blank=True)

    class Meta:
        db_table = "employers"

    def __str__(self):
        return self.company_name
