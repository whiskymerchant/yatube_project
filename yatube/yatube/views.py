from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    template = 'index.html'
    title = 'Awesome title'
    context = {
        'title': 'Это главная страница проекта Yatube',
        'text': 'Здесь будет информация о группах проекта Yatube'
        }
    return render(request, template, context) 

def group_posts(request, any):
    return HttpResponse('Здесь будет информация о группах проекта Yatube')

