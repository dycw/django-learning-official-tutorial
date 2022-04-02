import datetime as dt
from typing import cast

from beartype import beartype
from django.db.models import CASCADE
from django.db.models import CharField
from django.db.models import DateTimeField
from django.db.models import ForeignKey
from django.db.models import IntegerField
from django.db.models import Model
from django.utils.timezone import now


class Question(Model):  # type: ignore
    question_text = cast(str, CharField(max_length=200))
    pub_date = cast(dt.datetime, DateTimeField("date published"))

    @beartype
    def __str__(self) -> str:
        return self.question_text

    @beartype
    def was_published_recently(self) -> bool:
        return self.pub_date >= now() - dt.timedelta(days=1)


class Choice(Model):  # type: ignore
    question = cast(Question, ForeignKey(Question, on_delete=CASCADE))
    choice_text = cast(str, CharField(max_length=200))
    votes = cast(int, IntegerField(default=0))

    @beartype
    def __str__(self) -> str:
        return self.choice_text
