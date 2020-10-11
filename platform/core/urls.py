"""sustainable_urban_design_space URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path

from front_page.views import FrontPageView
from openstreetmap import urls as openstreetmap_urls
from patterns import urls as patterns_urls
from projects import urls as projects_urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    re_path(r"^i18n/", include("django.conf.urls.i18n")),
    path("openstreetmap/", include(openstreetmap_urls)),
    path("patterns/", include(patterns_urls)),
    path("projects/", include(projects_urls)),
    path("", FrontPageView.as_view(), name="front_page"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
