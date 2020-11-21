from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    first_name = None
    last_name = None
    profile = models.ForeignKey(
        to="users.UserProfile",
        null=True,
        blank=True,
        related_name="user",
        on_delete=models.SET_NULL,
    )


class UserProfile(models.Model):
    family_name = models.CharField(max_length=255, null=True, blank=True)
    given_name = models.CharField(max_length=255, null=True, blank=True)
    job_title = models.CharField(max_length=255, null=True, blank=True)