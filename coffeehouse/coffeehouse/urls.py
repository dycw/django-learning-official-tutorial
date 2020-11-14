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

from coffeehouse.about import views as about_views
from coffeehouse.stores import views as stores_views


urlpatterns = [
    path("admin/doc/", include("django.contrib.admindocs.urls")),
    path("admin/", admin.site.urls),
    path("", TemplateView.as_view(template_name="homepage.html")),
    path("about/", about_views.contact),
    path("stores/", stores_views.detail),
    path("stores/<int:store_id>/", stores_views.detail),
]
