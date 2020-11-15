from django import forms
from django.forms import ModelForm

from .models import AdministrativeDivision


class AdministrativeDivisionForm(ModelForm):
    class Meta:
        model = AdministrativeDivision
        fields = (
            "name",
            "description",
            "website",
            "division_type",
            "geographic_area",
        )
        widgets = {
            "geographic_area": forms.HiddenInput
        }
