from __future__ import annotations

from django.contrib.admin import site

from .models import Post


site.register(Post)
