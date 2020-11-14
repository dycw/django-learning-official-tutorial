"""coffeehouse URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from __future__ import annotations

from django.contrib import admin
from django.urls import include
from django.urls import path
from django.views.generic import TemplateView

from .about import views as about_views
from .stores import views as stores_views


about_patterns = [
    path("", about_views.index),
    path("contact/", about_views.contact),
]
admin_patterns = [
    path("", admin.site.urls),
    path("doc/", include("django.contrib.admindocs.urls")),
]
store_patterns = [
    path("", stores_views.index),
    path("<int:store_id>/", stores_views.detail),
]


urlpatterns = [
    path("", TemplateView.as_view(template_name="homepage.html")),
    path("admin/", include(admin_patterns)),
    path("about/", include(about_patterns)),
    path("stores/", include(store_patterns), {"location": "headquarters"}),
]
