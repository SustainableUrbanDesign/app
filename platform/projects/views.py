from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView, ListView

from .forms import ProjectForm
from .models import Project


class ProjectListView(ListView):
    model = Project
    context_object_name = "projects"
    template_name = "projects/projects.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["project_form"] = ProjectForm()
        return context


class ProjectView(DetailView):
    model = Project
    context_object_name = "project"
    template_name = "projects/project.html"


class EditProjectGoalsView(View):
    template_name = "projects/edit_project_goals.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
