from django.http import Http404
from django.shortcuts import render


def index(request):
    template = 'blog/index.html'
    context = {'posts': posts}
    return render(request, template, context)


def post_detail(request, post_id):
    template = 'blog/detail.html'
    context = None
    if post_id in post_data:
        context = {'post': post_data[post_id]}
    if context is None:
        raise Http404(f'Invalid value of the post_id = {post_id}')
    return render(request, template, context)


def category_posts(request, category_slug):
    template = 'blog/category.html'
    context = {'category': category_slug}
    return render(request, template, context)
