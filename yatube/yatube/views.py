from django.shortcuts import render


# Create your views here.
def index(request):
    template = 'index.html'
    title = 'This is the mainpage of the Yatube project'
    context = {
        'title': title,
    }
    return render(request, template, context)


def group_posts(request, any):
    template = 'index.html'
    title = 'This is posts'
    context = {
        'title': title,
    }
    return render(request, template, context)
