from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

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

    def post(self, request, *args, **kwargs):
        project_form = ProjectForm(request.POST)

        if project_form.is_valid():
            project = project_form.save()

            return redirect("project_view", pk=project.pk)
        else:
            context = {
                "project_form": project_form,
            }
            
            return render(request, self.template_name, context)


class ProjectDetailView(DetailView):
    model = Project
    context_object_name = "project"
    template_name = "projects/project.html"


class ProjectCreateView(CreateView):
    model = Project
    fields = ["title", "description",]


class ProjectUpdateView(UpdateView):
    model = Project
    context_object_name = "project"
    form_class = ProjectForm


class EditProjectGoalsView(View):
    template_name = "projects/edit_project_goals.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
