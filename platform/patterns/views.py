from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import DetailView, ListView

from .forms import UrbanDesignPatternForm
from .models import UrbanDesignPattern


class UrbanDesignPatternListView(ListView):
    model = UrbanDesignPattern
    context_object_name = "design_patterns"
    template_name = "patterns/patterns.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["pattern_form"] = UrbanDesignPatternForm()

        return context

    def post(self, request, *args, **kwargs):
        pattern_form = UrbanDesignPatternForm(request.POST)

        if pattern_form.is_valid():
            pattern = pattern_form.save()

            return redirect("pattern_view", pk=pattern.pk)
        else:
            context = {
                "pattern_form": pattern_form,
            }
            
            return render(request, self.template_name, context)


class UrbanDesignPatternView(DetailView):
    model = UrbanDesignPattern
    context_object_name = "pattern"
    template_name = "patterns/pattern.html"
