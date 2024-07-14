# در فایل admin.py در بخش blog
from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_posted')
    search_fields = ['title', 'content']
    list_filter = ['date_posted']


admin.site.register(Post, PostAdmin)
