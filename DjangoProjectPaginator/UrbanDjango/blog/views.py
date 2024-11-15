from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Post


def post_list(request):
    posts = Post.objects.all()

    per_page = int(request.GET.get('per_page', 10))


    paginator = Paginator(posts, per_page)

    page_number = request.GET.get('page')

    try:
        page_posts = paginator.get_page(page_number)
    except PageNotAnInteger:
        page_posts = paginator.page(1)
    except EmptyPage:
        page_posts = paginator.page(paginator.num_pages)

    return render(
        request,
        'post_list.html',
        {
            'page_posts': page_posts,
            'per_page': per_page,
        }
    )