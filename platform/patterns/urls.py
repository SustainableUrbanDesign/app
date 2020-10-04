from django.urls import path

from .views import (
    UrbanDesignPatternListView,
    UrbanDesignPatternView,
    UrbanDesignPatternTagView,
)

urlpatterns = [
    path(
        "tagged/<tag>/", UrbanDesignPatternTagView.as_view(), name="pattern_tag_view",
    ),
    path("<int:pk>/", UrbanDesignPatternView.as_view(), name="pattern_view"),
    path("", UrbanDesignPatternListView.as_view(), name="patterns_list"),
]
