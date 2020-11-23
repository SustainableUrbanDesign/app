from django.urls import path

from .views import (
    UserProfileListView,
    UserProfileCreateView,
    UserProfileDetailView,
    UserProfileUpdateView,
)

urlpatterns = [
    path("create/", UserProfileCreateView.as_view(), name="user_profile_create_view"),
    path("<int:pk>/", UserProfileDetailView.as_view(), name="user_profile_view"),
    path("<int:pk>/edit/", UserProfileUpdateView.as_view(), name="user_profile_update_view"),
    path("", UserProfileListView.as_view(), name="user_profiles_list"),
]
