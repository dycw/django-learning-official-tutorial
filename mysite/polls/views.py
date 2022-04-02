from beartype import beartype
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse


@beartype
def index(_: WSGIRequest) -> HttpResponse:
    return HttpResponse("Hello, world. You're at the polls index.")


@beartype
def detail(_: WSGIRequest, question_id: int) -> HttpResponse:
    return HttpResponse(f"You're looking at question {question_id}.")


@beartype
def results(_: WSGIRequest, question_id: int) -> HttpResponse:
    return HttpResponse(
        f"You're looking at the results of question {question_id}."
    )


@beartype
def vote(_: WSGIRequest, question_id: int) -> HttpResponse:
    return HttpResponse(f"You're voting on question {question_id}")
