from django.contrib.gis import admin

from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.OSMGeoAdmin):
    pass
