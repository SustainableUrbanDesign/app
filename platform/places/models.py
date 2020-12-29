from django.contrib.gis.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse

from mptt.models import MPTTModel, TreeForeignKey


class DivisionTypeChoices(models.TextChoices):
    DISTRICT = "district", _("District")
    MUNICIPALITY = "municipality", _("Municipality")


class Place(MPTTModel):
    name = models.CharField(max_length=255)
    description = models.TextField()
    website = models.URLField()
    division_type = models.CharField(max_length=255, choices=DivisionTypeChoices.choices)
    parent = TreeForeignKey(
        "self", on_delete=models.PROTECT, null=True, blank=True, related_name="children"
    )
    geographic_area = models.PolygonField(geography=True, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("place_view", kwargs={"pk": self.pk,})