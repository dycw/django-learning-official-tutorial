from __future__ import annotations

from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def detail(
    request: WSGIRequest,
    store_id: int = 1,  # noqa: U100
) -> HttpResponse:
    # Access store_id with 'store_id' variable
    return render(request, "stores/detail.html")
