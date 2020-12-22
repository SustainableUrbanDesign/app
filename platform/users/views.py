from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView

from .forms import UserProfileForm
from .models import UserProfile


class UserProfileListView(ListView):
    model = UserProfile
    context_object_name = "profiles"
    template_name = "users/profiles.html"


class UserProfileDetailView(DetailView):
    model = UserProfile
    context_object_name = "profile"
    template_name = "users/profile.html"


# TODO: consider whether/how to convert this to a class-based view
@login_required
def edit_profile(request):
    if request.method == "POST":
        profile_form = UserProfileForm(
            instance=request.user.profile,
            data=request.POST,
        )

        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, "Profile saved")
        else:
            messages.error(request, "Error saving profile")
    else:
        profile_form = UserProfileForm(instance=request.user.profile)

    return render(request, "users/my_profile.html", {"profile_form": profile_form})
