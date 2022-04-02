from beartype import beartype
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.template.loader import get_template
from polls.models import Question


@beartype
def index(request: WSGIRequest) -> HttpResponse:
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    template = get_template("polls/index.html")
    context = {"latest_question_list": latest_question_list}
    return HttpResponse(template.render(context, request))


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
    return HttpResponse(f"You're voting on question {question_id}.")
