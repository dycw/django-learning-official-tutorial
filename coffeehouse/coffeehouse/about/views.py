from __future__ import annotations

from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.


def contact(request: WSGIRequest) -> HttpResponse:
    # Content from request or database extracted here
    # and passed to the template for display
    return render(request, "about/contact.html")
