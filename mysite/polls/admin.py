from typing import TYPE_CHECKING
from typing import Any

from django.contrib.admin import ModelAdmin as _ModelAdmin
from django.contrib.admin import StackedInline as _StackedInline
from django.contrib.admin import TabularInline as _TabularInline
from django.contrib.admin import site
from polls.models import Choice
from polls.models import Question


ModelAdmin = _ModelAdmin[Any] if TYPE_CHECKING else _ModelAdmin
StackedInline = _StackedInline[Any] if TYPE_CHECKING else _StackedInline
TabularInline = _TabularInline[Any] if TYPE_CHECKING else _TabularInline


class ChoiceInline(TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"]}),
    ]
    inlines = [ChoiceInline]
    list_display = ("question_text", "pub_date", "was_published_recently")
    list_filter = ["pub_date"]
    search_fields = ["question_text"]


site.register(Question, QuestionAdmin)
