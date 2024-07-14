# در فایل views.py
from django.views.generic import ListView, DetailView
from .models import Post


class PostListView(ListView):
    model = Post
    template_name = 'blog/blog_home.html'  # تنظیم نام تمپلیت
    context_object_name = 'posts'  # تنظیم نام شیء در کانتکست


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'  # تنظیم نام تمپلیت
    context_object_name = 'post'  # تنظیم نام شیء در کانتکست
