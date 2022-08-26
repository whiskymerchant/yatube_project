# posts/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('group_posts/', views.group_posts, name='group_posts'),
    
] 

app_name = 'posts'