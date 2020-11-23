from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView

#from .forms import UserProfileForm
from .models import UserProfile


class UserProfileListView(ListView):
    model = UserProfile
    context_object_name = "profiles"
    template_name = "users/profiles.html"


class UserProfileDetailView(DetailView):
    model = UserProfile
    context_object_name = "profile"
    template_name = "users/profile.html"


class UserProfileCreateView(CreateView):
    model = UserProfile
    template_name = "users/profile_form.html"
    #form_class = UserProfileForm
    fields = ("given_name", "family_name", "job_title")


class UserProfileUpdateView(UpdateView):
    model = UserProfile
    context_object_name = "profile"
    template_name = "users/profile_form.html"
    #form_class = UserProfileForm
    fields = ("given_name", "family_name", "job_title")
