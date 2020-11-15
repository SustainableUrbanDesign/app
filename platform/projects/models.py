from django.contrib.gis.db import models
from django.contrib.gis.forms.widgets import OSMWidget
from django.urls import reverse


class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    geographic_area = models.PolygonField(geography=True, null=True, blank=True)
    administrative_division = models.ForeignKey(
        to="administrative_divisions.AdministrativeDivision",
        on_delete=models.SET_NULL,
        related_name="projects",
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("project_view", kwargs={"pk": self.pk,})
