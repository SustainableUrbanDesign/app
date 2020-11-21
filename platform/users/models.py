from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    first_name = None
    last_name = None


class UserProfile(models.Model):
    family_name = models.CharField(max_length=255, null=True, blank=True)
    given_name = models.CharField(max_length=255, null=True, blank=True)
    job_title = models.CharField(max_length=255, null=True, blank=True)