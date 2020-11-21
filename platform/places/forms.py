from django import forms
from django.forms import ModelForm

from .models import Place


class PlaceForm(ModelForm):
    class Meta:
        model = Place
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
