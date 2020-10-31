from django import forms
from django.forms import ModelForm
from django.contrib.gis.forms import OSMWidget

from .models import Project


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ("title", "description", "geographic_area")
        widgets = {
            "geographic_area": forms.HiddenInput
        }
