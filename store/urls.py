from django.urls import path
from .views import HomeView, ProductDetailView, ExoticView, GgView, TikiView, FreshView, HolyView, CompoundView, \
    ClearwaterView, CiphergeneticsView, BloomseedsView, RkiemView, BarnysView, GreenhouseView, SeriousView, \
    ZmoothiezView, EthosView ,ThirdView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product.detail'),
    path('exotic/', ExoticView.as_view(), name='exotic'),
    path('gg/', GgView.as_view(), name='gg'),
    path('tiki/', TikiView.as_view(), name='tiki'),
    path('freshcoast/', FreshView.as_view(), name='freshcoast'),
    path('holysmoke/', HolyView.as_view(), name='holysmoke'),
    path('compound/', CompoundView.as_view(), name='compound'),
    path('clearwater/', ClearwaterView.as_view(), name='clearwater'),
    path('ciphergenetic/', CiphergeneticsView.as_view(), name='ciphergenetic'),
    path('bloomseeds/', BloomseedsView.as_view(), name='bloomseeds'),
    path('r-kiem/', RkiemView.as_view(), name='rkiem'),
    path('barnysfarm/', BarnysView.as_view(), name='barnys'),
    path('greenhouse/', GreenhouseView.as_view(), name='green'),
    path('seriousseeds/', SeriousView.as_view(), name='serious'),
    path('zmoothiez/', ZmoothiezView.as_view(), name='zmoothiez'),
    path('ethos/', EthosView.as_view(), name='ethos'),
    path('3rd/', ThirdView.as_view(), name='3rd'),
]
