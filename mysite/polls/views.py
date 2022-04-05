from typing import TYPE_CHECKING

from beartype import beartype
from django.db.models.query import QuerySet
from django.http import HttpRequest
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.urls import reverse
from django.utils.timezone import now
from django.views.generic import DetailView as _DetailView
from django.views.generic import ListView as _ListView
from polls.models import Choice
from polls.models import Question


if TYPE_CHECKING:
    ListViewQuestion = _ListView[Question]
    DetailViewQuestion = _DetailView[Question]
else:
    ListViewQuestion = _ListView
    DetailViewQuestion = _DetailView


class IndexView(ListViewQuestion):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    @beartype
    def get_queryset(self) -> QuerySet[Question]:
        return Question.objects.filter(pub_date__lte=now()).order_by(
            "-pub_date"
        )[:5]


class DetailView(DetailViewQuestion):
    model = Question
    template_name = "polls/detail.html"


class ResultsView(DetailViewQuestion):
    model = Question
    template_name = "polls/results.html"


@beartype
def vote(request: HttpRequest, question_id: int) -> HttpResponse:
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice: Choice = question.choice_set.get(  # type: ignore
            pk=request.POST["choice"]
        )
    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    selected_choice.votes += 1
    selected_choice.save()
    return HttpResponseRedirect(reverse("polls:results", args=(question_id,)))
