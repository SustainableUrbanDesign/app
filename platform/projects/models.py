from django.contrib.gis.db import models
from django.urls import reverse

from wagtail.admin.edit_handlers import FieldPanel, RichTextFieldPanel
from wagtail.core.fields import RichTextField


class Project(models.Model):
    title = models.CharField(max_length=255)
    description = RichTextField(features=["h2", "h3", "bold", "italic", "link"])
    geographic_area = models.PolygonField(geography=True, null=True, blank=True)

    panels = [
        FieldPanel("title"),
        RichTextFieldPanel("description"),
    ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("project_view", kwargs={"pk": self.pk,})
