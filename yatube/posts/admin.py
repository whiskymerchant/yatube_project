from django.contrib import admin
from .models import Post, Group


class PostAdmin(admin.ModelAdmin):
    # Перечисляем поля, которые должны отображаться в админке
    list_display = ('pk', 'text', 'pub_date', 'author', 'group',) 
    # Добавляем интерфейс для поиска по тексту постов
    list_editable = ('group',)
    search_fields = ('text',) 
    # Добавляем возможность фильтрации по дате
    list_filter = ('pub_date',) 
    empty_value_display = '-пусто-'


class GroupAdmin(admin.ModelAdmin):
    pass


admin.site.register(Post, PostAdmin)
admin.site.register(Group)


# Register your models here
