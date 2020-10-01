from django.urls import path

from .views import EditProjectGoalsView, ProjectListView, ProjectView

urlpatterns = [
    path("<int:pk>/", ProjectView.as_view(), name="project_view"),
    path("<int:pk>/goals/", EditProjectGoalsView.as_view(), name="project_goals_view"),
    path("", ProjectListView.as_view()),
]
