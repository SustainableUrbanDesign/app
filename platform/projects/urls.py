from django.urls import path

from .views import ProjectListView, ProjectView

urlpatterns = [
    path("<int:pk>/", ProjectView.as_view()),
    path("", ProjectListView.as_view())
]