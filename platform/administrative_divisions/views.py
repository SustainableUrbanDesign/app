from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView

from .models import AdministrativeDivision


class AdministrativeDivisionListView(ListView):
    model = AdministrativeDivision
    context_object_name = "administrative_divisions"
    template_name = "administrative_divisions/administrative_divisions.html"


class AdministrativeDivisionDetailView(DetailView):
    model = AdministrativeDivision
    context_object_name = "administrative_division"
    template_name = "administrative_divisions/administrative_division.html"


class AdministrativeDivisionCreateView(CreateView):
    model = AdministrativeDivision
    template_name = "administrative_divisions/administrative_division_form.html"
    fields = [
        "name",
        "description",
        "website",
        "division_type",
    ]


class AdministrativeDivisionUpdateView(UpdateView):
    model = AdministrativeDivision
    context_object_name = "administrative_division"
    template_name = "administrative_divisions/administrative_division_form.html"
    fields = [
        "name",
        "description",
        "website",
        "division_type",
    ]
