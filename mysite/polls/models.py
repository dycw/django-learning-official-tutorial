from typing import Any
from typing import cast

from django.db.models import CASCADE
from django.db.models import CharField
from django.db.models import DateTimeField
from django.db.models import ForeignKey
from django.db.models import IntegerField
from django.db.models import Model


class Question(Model):  # type: ignore
    question_text: Any = CharField(max_length=200)
    pub_date: Any = DateTimeField("date published")


class Choice(Model):  # type: ignore
    question = cast(Question, ForeignKey(Question, on_delete=CASCADE))
    choice_text = cast(str, CharField(max_length=200))
    votes = cast(int, IntegerField(default=0))
