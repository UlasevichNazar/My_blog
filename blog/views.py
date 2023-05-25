from django.shortcuts import render, get_object_or_404
from django.http import Http404

from blog.models import Post


def post_list(request):
    post = Post.published.all()
    return render(request, 'blog/post/list.html', {'post': post})


def post_detail(request, id):
    post = get_object_or_404(Post, pk=id, status=Post.Status.PUBLISHED)
    # try:
    #     post=Post.published.get(pk=id)
    # except Post.DoesNotExist:
    #     raise Http404("No Post found")

    return render(request, 'blog/post/detail.html', {'post': post})
