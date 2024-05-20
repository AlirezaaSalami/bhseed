from django.views.generic import ListView, DetailView , TemplateView
from .models import Product


class HomeView(ListView):
    model = Product
    template_name = 'home.html'
    context_object_name = 'products'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'


class ExoticView(TemplateView):
    template_name = 'exotic.html'