from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView, ListView

from .models import UrbanDesignPattern, UrbanDesignPatternTag


class UrbanDesignPatternListView(ListView):
    model = UrbanDesignPattern
    context_object_name = "design_patterns"
    template_name = "patterns/patterns.html"


class UrbanDesignPatternView(DetailView):
    model = UrbanDesignPattern
    context_object_name = "pattern"
    template_name = "patterns/pattern.html"


class UrbanDesignPatternTagView(DetailView):
    model = UrbanDesignPatternTag
    context_object_name = "tag"
    template_name = "patterns/tag.html"
    slug_field = "tag"
    slug_url_kwarg = "tag"

    def get_object(self):
        return UrbanDesignPatternTag.objects.get(tag=self.kwargs.get("tag"))
