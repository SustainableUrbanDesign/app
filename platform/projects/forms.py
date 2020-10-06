from django.forms import ModelForm
from django.contrib.gis.forms import OSMWidget

from .models import Project


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ("title", "description")
        # TODO: determine how to get the 'geographic_area' field to render correctly in a Bootstrap modal
