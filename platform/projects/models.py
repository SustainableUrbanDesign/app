from django.db import models
from wagtail.admin.edit_handlers import (
    FieldPanel,
    RichTextFieldPanel 
)
from wagtail.core.fields import RichTextField


class Project(models.Model):
    title = models.CharField(max_length=255)
    description = RichTextField()

    panels = [
        FieldPanel("title"),
        RichTextFieldPanel("description"),
    ]

    def __str__(self):
        return self.title