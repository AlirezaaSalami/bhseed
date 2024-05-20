from django.urls import path
from .views import HomeView, ProductDetailView, ExoticView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product.detail'),
    path('exotic/', ExoticView.as_view(), name='exotic'),
]
