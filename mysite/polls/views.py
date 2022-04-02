from beartype import beartype
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse


@beartype
def index(_: WSGIRequest) -> HttpResponse:
    return HttpResponse("Hello, world. You're at the polls index.")
