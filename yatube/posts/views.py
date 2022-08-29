from django.shortcuts import get_object_or_404, render

from posts.models import Post, Group


# Create your views here.
def index(request):
    template = 'posts/index.html'
    posts = Post.objects.order_by('-pub_date')[:10]
    title = 'You are in posts'
    context = {
        'posts': posts,
        'title': title,
    }
    return render(request, template, context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    template = 'posts/group_list.html'
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    title = 'This is the group post'
    context = {
        'group': group,
        'posts': posts,
        'title': title,
    }
    return render(request, template, context)
