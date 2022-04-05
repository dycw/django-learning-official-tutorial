from typing import TYPE_CHECKING
from typing import Any

from django.contrib import admin
from django.contrib.admin import ModelAdmin as _ModelAdmin
from django.contrib.admin import StackedInline as _StackedInline
from polls.models import Choice
from polls.models import Question


ModelAdmin = _ModelAdmin[Any] if TYPE_CHECKING else _ModelAdmin
StackedInline = _StackedInline[Any] if TYPE_CHECKING else _StackedInline


class ChoiceInline(StackedInline):
    model = Choice
    extra = 3


class QuestionAdmin(ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"]}),
    ]
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)
