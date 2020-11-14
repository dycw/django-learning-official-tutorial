from __future__ import annotations

from django.core.handlers.wsgi import WSGIRequest
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.views.generic import ListView

from .forms import EmailPostForm
from .models import Post


class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = "posts"
    paginate_by = 3
    template_name = "blog/post/list.html"


def post_list(request: WSGIRequest) -> HttpResponse:
    object_list = Post.published.all()
    paginator = Paginator(object_list, 3)  # 3 posts in each page
    page = request.GET.get("page")
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
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


def post_share(request: WSGIRequest, post_id: int) -> HttpResponse:
    # Retrieve post by id
    post = get_object_or_404(Post, id=post_id, status="published")
    if request.method == "POST":
        # Form was submitted
        form = EmailPostForm(request.POST)
        if form.is_valid():
            # Form fields passed validation
            form.cleaned_data
            # ... send email
    else:
        form = EmailPostForm()
    return render(
        request,
        "blog/post/share.html",
        {
            "post": post,
            "form": form,
        },
    )
