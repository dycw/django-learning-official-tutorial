from __future__ import annotations

from django.urls import path

from .views import post_detail
from .views import post_list


app_name = "blog"
urlpatterns = [
    # post views
    path("", post_list, name="post_list"),
    path(
        "<int:year>/<int:month>/<int:day>/<slug:post>/",
        post_detail,
        name="post_detail",
    ),
]
