from __future__ import annotations

from typing import Optional

from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.


def detail(
    request: WSGIRequest,
    store_id: int = 1,  # noqa: U100
    location: Optional[str] = None,
) -> HttpResponse:
    if location is None:
        raise ValueError("Expected a value for 'location'; got None")
    # Access store_id param with 'store_id' variable and location param with
    # 'location' variable
    # Extract 'hours' or 'map' value appended to url as
    # ?hours=sunday&map=flash
    request.GET.get("hours", "")
    request.GET.get("map", "")
    # given /stores/1/?hours=sunday&map=flash,
    #   'hours' has value 'sunday' or '' if hours not in url
    #   'map' has value 'flash' or '' if map not in url
    return render(request, "stores/detail.html")


def index(request: WSGIRequest) -> HttpResponse:
    return render(request, "stores/index.html")
