from django.contrib.gis import admin

from .models import AdministrativeDivision


@admin.register(AdministrativeDivision)
class AdministrativeDivisionAdmin(admin.OSMGeoAdmin):
    pass
