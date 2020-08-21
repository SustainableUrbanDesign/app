from django.shortcuts import render

from django.views.generic import DetailView, ListView

from .models import Project

class ProjectListView(ListView):
    model = Project
    context_object_name = "projects"
    template_name = "projects/projects.html"


class ProjectView(DetailView):
    model = Project
    context_object_name = "project"
    template_name = "projects/project.html"