from django.urls import path

from .views import (
    EditProjectGoalsView,
    ProjectListView,
    ProjectCreateView,
    ProjectDetailView,
    ProjectUpdateView,
)

urlpatterns = [
    path("create/", ProjectCreateView.as_view(), name="project_create_view"),
    path("<int:pk>/", ProjectDetailView.as_view(), name="project_view"),
    path("<int:pk>/goals/", EditProjectGoalsView.as_view(), name="project_goals_view"),
    path("<int:pk>/edit/", ProjectUpdateView.as_view(), name="project_update_view"),
    path("", ProjectListView.as_view(), name="projects_list"),
]
