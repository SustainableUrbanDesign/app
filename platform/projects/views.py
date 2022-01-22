from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView

from .forms import ProjectForm
from .models import Project


class ProjectListView(ListView):
    model = Project
    context_object_name = "projects"
    template_name = "projects/projects.html"


class ProjectDetailView(DetailView):
    model = Project
    context_object_name = "project"
    template_name = "projects/project.html"


class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectForm


class ProjectUpdateView(UpdateView):
    model = Project
    context_object_name = "project"
    form_class = ProjectForm


class EditProjectGoalsView(DetailView):
    template_name = "projects/edit_project_goals.html"
    model = Project
