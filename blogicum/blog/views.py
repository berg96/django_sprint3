from django.http import Http404
from django.shortcuts import render, get_object_or_404
from blog.models import Post, Category
from datetime import datetime


def index(request):
    template = 'blog/index.html'
    post_list = Post.objects.filter(
        is_published=True,
        category__is_published=True,
        pub_date__lte=datetime.now()
    ).order_by('-pub_date')[0:5]
    context = {'post_list': post_list}
    return render(request, template, context)


def post_detail(request, pk):
    template = 'blog/detail.html'
    post = Post.objects.get(pk=pk)
    context = {'post': post}
    return render(request, template, context)


def category_posts(request, category_slug):
    template = 'blog/category.html'
    #post_list = get_object_or_404(Post.objects.select_related('category').filter(
    #    is_published=True,
    #    category__slug=category_slug,
    #    pub_date__lte=datetime.now()
    #).order_by('-pub_date'), category__is_published=True)
    #context = {'post_list': post_list}
    return render(request, template, context)
