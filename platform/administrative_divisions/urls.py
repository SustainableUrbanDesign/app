from django.urls import path

from .views import (
    AdministrativeDivisionListView,
    AdministrativeDivisionCreateView,
    AdministrativeDivisionDetailView,
    AdministrativeDivisionUpdateView,
)

urlpatterns = [
    path("create/", AdministrativeDivisionCreateView.as_view(), name="administrative_division_create_view"),
    path("<int:pk>/", AdministrativeDivisionDetailView.as_view(), name="administrative_division_view"),
    path("<int:pk>/edit/", AdministrativeDivisionUpdateView.as_view(), name="administrative_division_update_view"),
    path("", AdministrativeDivisionListView.as_view(), name="administrative_divisions_list"),
]
