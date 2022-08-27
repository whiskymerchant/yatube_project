from turtle import title
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    posts = Post.objects.order_by('-pub_date')[:10]
    title = 'You are in posts'
    context = {
        'posts': posts,
        'title': title,
    }
    return render(request, 'posts/index.html', context) 


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    title = 'This is the group post'
    context = {
        'group': group,
        'posts': posts,
        'title': title,
    }
    return render(request, 'posts/group_list.html', context) 