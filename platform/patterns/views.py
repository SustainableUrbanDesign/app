from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView, ListView

from .models import UrbanDesignPattern


class UrbanDesignPatternListView(ListView):
    model = UrbanDesignPattern
    context_object_name = "design_patterns"
    template_name = "patterns/patterns.html"


class UrbanDesignPatternView(DetailView):
    model = UrbanDesignPattern
    context_object_name = "pattern"
    template_name = "patterns/pattern.html"
