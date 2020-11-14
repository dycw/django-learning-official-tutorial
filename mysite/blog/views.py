from __future__ import annotations

from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render

from .models import Post


def post_list(request: WSGIRequest) -> HttpResponse:
    posts = Post.published.all()
    return render(
        request,
        "blog/post/list.html",
        {"posts": posts},
    )


def post_detail(
    request: WSGIRequest,
    year: int,
    month: int,
    day: int,
    post: str,
) -> HttpResponse:
    post = get_object_or_404(
        Post,
        slug=post,
        status="published",
        publish__year=year,
        publish__month=month,
        publish__day=day,
    )
    return render(
        request,
        "blog/post/detail.html",
        {"post": post},
    )
