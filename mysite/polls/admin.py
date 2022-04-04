from typing import Any
from typing import cast

from django.contrib import admin
from polls.models import Question


cast(Any, admin.site).register(Question)
