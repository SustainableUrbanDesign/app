from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView

from .forms import PlaceForm
from .models import Place


class PlaceListView(ListView):
    model = Place
    context_object_name = "places"
    template_name = "places/places.html"


class PlaceDetailView(DetailView):
    model = Place
    context_object_name = "place"
    template_name = "places/place.html"


class PlaceCreateView(CreateView):
    model = Place
    template_name = "places/place_form.html"
    form_class = PlaceForm


class PlaceUpdateView(UpdateView):
    model = Place
    context_object_name = "place"
    template_name = "places/place_form.html"
    form_class = PlaceForm
