import datetime as dt
from typing import Any
from typing import Callable
from typing import TypeVar
from typing import cast

from beartype import beartype
from django.contrib.admin import display as _display
from django.db.models import CASCADE
from django.db.models import CharField
from django.db.models import DateTimeField
from django.db.models import ForeignKey
from django.db.models import IntegerField
from django.db.models import Model
from django.utils.timezone import now


_TCallable = TypeVar("_TCallable", bound=Callable[..., Any])
display = cast(Callable[..., Callable[[_TCallable], _TCallable]], _display)


class Question(Model):
    question_text = cast(str, CharField(max_length=200))
    pub_date = cast(dt.datetime, DateTimeField("date published"))

    @beartype
    def __str__(self) -> str:
        return self.question_text

    @beartype
    @display(
        boolean=True, ordering="pub_date", description="Published recently?"
    )
    def was_published_recently(self) -> bool:
        dt_now = now()
        return dt_now - dt.timedelta(days=1) <= self.pub_date <= dt_now


class Choice(Model):
    question = cast(Question, ForeignKey(Question, on_delete=CASCADE))
    choice_text = cast(str, CharField(max_length=200))
    votes = cast(int, IntegerField(default=0))

    @beartype
    def __str__(self) -> str:
        return self.choice_text
