from django import forms
from django.forms import ModelForm

from .models import Project


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ("title", "description", "geographic_area", "administrative_division")
        widgets = {
            "geographic_area": forms.HiddenInput
        }
