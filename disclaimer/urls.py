from django.urls import path
from .views import DisclaimerView

urlpatterns = [
    path('', DisclaimerView.as_view()),
]
