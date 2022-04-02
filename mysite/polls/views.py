from beartype import beartype
from django.http import HttpResponse
from django.http.request import HttpRequest
from django.shortcuts import render
from polls.models import Question


@beartype
def index(request: HttpRequest) -> HttpResponse:
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)


@beartype
def detail(_: HttpRequest, question_id: int) -> HttpResponse:
    return HttpResponse(f"You're looking at question {question_id}.")


@beartype
def results(_: HttpRequest, question_id: int) -> HttpResponse:
    return HttpResponse(
        f"You're looking at the results of question {question_id}."
    )


@beartype
def vote(_: HttpRequest, question_id: int) -> HttpResponse:
    return HttpResponse(f"You're voting on question {question_id}.")
