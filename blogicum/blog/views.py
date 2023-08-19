from datetime import datetime

from django.shortcuts import render, get_object_or_404

from blog.models import Post, Category


def pub_post_filter(posts):
    return posts.filter(
        is_published=True,
        category__is_published=True,
        pub_date__lte=datetime.now()
    )


def index(request):
    post_list = pub_post_filter(Post.objects.select_related(
        'location',
        'category',
        'author'
    ))[0:5]
    return render(request, 'blog/index.html', {'post_list': post_list})


def post_detail(request, post_id):
    post = get_object_or_404(
        pub_post_filter(Post.objects.select_related(
            'location',
            'category',
            'author'
        )),
        pk=post_id
    )
    return render(request, 'blog/detail.html', {'post': post})


def category_posts(request, category_slug):
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )
    post_list = pub_post_filter(category.posts.select_related(
        'location',
        'category',
        'author'
    ))
    return render(
        request,
        'blog/category.html',
        {'category': category,'post_list': post_list, }
    )
