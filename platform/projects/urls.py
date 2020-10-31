from django.urls import path

from .views import (
    EditProjectGoalsView,
    ProjectListView,
    ProjectDetailView,
)

urlpatterns = [
    path("<int:pk>/", ProjectDetailView.as_view(), name="project_detail_view"),
    path("<int:pk>/goals/", EditProjectGoalsView.as_view(), name="project_goals_view"),
    path("", ProjectListView.as_view(), name="projects_list"),
]
