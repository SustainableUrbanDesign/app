from django.db import models
from django.utils.translation import gettext_lazy as _

from mptt.models import MPTTModel, TreeForeignKey


class DivisionTypeChoices(models.TextChoices):
    DISTRICT = "district", _("District")
    MUNICIPALITY = "municipality", _("Municipality")


class AdministrativeDivision(MPTTModel):
    name = models.CharField(max_length=255)
    description = models.TextField()
    website = models.URLField()
    division_type = models.CharField(max_length=255, choices=DivisionTypeChoices.choices)
    parent = TreeForeignKey(
        "self", on_delete=models.PROTECT, null=True, blank=True, related_name="children"
    )

    def __str__(self):
        return self.name