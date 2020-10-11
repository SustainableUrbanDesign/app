from django.forms import ModelForm
from django.contrib.gis.forms import OSMWidget

from .models import UrbanDesignPattern


class UrbanDesignPatternForm(ModelForm):
    class Meta:
        model = UrbanDesignPattern
        fields = ("title", "description", "keywords",)
        