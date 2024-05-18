from django.urls import path
from .views import HomeView, ProductDetailView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product.detail'),
]
