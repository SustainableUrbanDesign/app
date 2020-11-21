from django.urls import path

from .views import (
    PlaceListView,
    PlaceCreateView,
    PlaceDetailView,
    PlaceUpdateView,
)

urlpatterns = [
    path("create/", PlaceCreateView.as_view(), name="place_create_view"),
    path("<int:pk>/", PlaceDetailView.as_view(), name="place_view"),
    path("<int:pk>/edit/", PlaceUpdateView.as_view(), name="place_update_view"),
    path("", PlaceListView.as_view(), name="places_list"),
]
