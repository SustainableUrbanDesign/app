from django.urls import path

from .views import (
    UrbanDesignPatternListView,
    UrbanDesignPatternView,
)

urlpatterns = [
    path("<int:pk>/", UrbanDesignPatternView.as_view(), name="pattern_view"),
    path("", UrbanDesignPatternListView.as_view(), name="patterns_list"),
]
