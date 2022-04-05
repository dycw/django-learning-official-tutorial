import datetime as dt
from typing import cast

from beartype import beartype
from django.test import TestCase
from django.urls import reverse
from django.utils.timezone import now
from polls.models import Question


class QuestionModelTests(TestCase):
    @beartype
    def test_was_published_recently_with_future_question(self) -> None:
        """was_published_recently() returns False for questions whose pub_date
        is in the future.
        """

        time = now() + dt.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertFalse(future_question.was_published_recently())

    @beartype
    def test_was_published_recently_with_old_question(self) -> None:
        """was_published_recently() returns False for questions whose pub_date
        is older than 1 day.
        """

        time = now() - dt.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertFalse(old_question.was_published_recently())

    @beartype
    def test_was_published_recently_with_recent_question(self) -> None:
        """was_published_recently() returns True for questions whose pub_date
        is within the last day.
        """

        time = now() - dt.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertTrue(recent_question.was_published_recently())


@beartype
def create_question(question_text: str, days: int) -> Question:
    """Create a question with the given `question_text` and published the given
    number of `days` offset to now (negative for questions published in the
    past, positive for questions that have yet to be published).
    """

    time = now() + dt.timedelta(days=days)
    return cast(
        Question,
        Question.objects.create(question_text=question_text, pub_date=time),
    )


class QuestionIndexViewTests(TestCase):
    @beartype
    def test_no_questions(self) -> None:
        """If no questions exist, an appropriate message is displayed."""

        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context["latest_question_list"], [])

    @beartype
    def test_past_question(self) -> None:
        """Questions with a pub_date in the past are displayed on the index
        page.
        """

        question = create_question(question_text="Past question.", days=-30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerysetEqual(
            response.context["latest_question_list"], [question]
        )

    @beartype
    def test_future_question(self) -> None:
        """Questions with a pub_date in the future aren't displayed on the
        index page.
        """

        _ = create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse("polls:index"))
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context["latest_question_list"], [])

    @beartype
    def test_future_question_and_past_question(self) -> None:
        """Even if both past and future questions exist, only past questions
        are displayed.
        """

        question = create_question(question_text="Past question.", days=-30)
        _ = create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerysetEqual(
            response.context["latest_question_list"], [question]
        )

    @beartype
    def test_two_past_questions(self) -> None:
        """The questions index page may display multiple questions."""

        question1 = create_question(question_text="Past question 1.", days=-30)
        question2 = create_question(question_text="Past question 2.", days=-5)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerysetEqual(
            response.context["latest_question_list"], [question2, question1]
        )
