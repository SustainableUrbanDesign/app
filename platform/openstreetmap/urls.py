from django.urls import path

from . import views

urlpatterns = [
    path("data", views.get_osm_data, name="get_osm_data"),
]
