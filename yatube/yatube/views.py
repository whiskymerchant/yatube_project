from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return HttpResponse('Главная страница')


def group_posts(request, any):
    return HttpResponse('All the group posts are here')