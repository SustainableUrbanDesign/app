from django.db import models
from wagtail.core.models import Page


class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title