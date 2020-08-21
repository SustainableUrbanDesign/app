from django.urls import path

from .views import ProjectListView, ProjectView

urlpatterns = [
    path(
        "<int:pk>/",
        ProjectView.as_view(),
        name="project_view"
    ),
    path("", ProjectListView.as_view())
]