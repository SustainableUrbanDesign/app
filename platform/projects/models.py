from django.db import models
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.models import Page


class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    panels = [
        FieldPanel('title'),
        FieldPanel('description'),
    ]

    def __str__(self):
        return self.title