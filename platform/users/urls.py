from django.urls import path

from .views import (
    edit_profile,
    UserProfileListView,
    UserProfileDetailView,
)

urlpatterns = [
    path("me/", edit_profile, name="my_profile_view"),
    path("<int:pk>/", UserProfileDetailView.as_view(), name="user_profile_view"),
    path("", UserProfileListView.as_view(), name="user_profiles_list"),
]
