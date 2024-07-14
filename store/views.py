from django.views.generic import ListView, DetailView, TemplateView
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


class GgView(TemplateView):
    template_name = 'gg.html'


class TikiView(TemplateView):
    template_name = 'tiki.html'


class FreshView(TemplateView):
    template_name = 'freshcoast.html'


class HolyView(TemplateView):
    template_name = 'holy.html'


class CompoundView(TemplateView):
    template_name = 'compound.html'


class ClearwaterView(TemplateView):
    template_name = 'cw.html'


class CiphergeneticsView(TemplateView):
    template_name = 'cg.html'


class BloomseedsView(TemplateView):
    template_name = 'bloomseeds.html'


class RkiemView(TemplateView):
    template_name = 'rkiem.html'


class BarnysView(TemplateView):
    template_name = 'barnys.html'


class GreenhouseView(TemplateView):
    template_name = 'green.html'


class SeriousView(TemplateView):
    template_name = 'serious.html'


class ZmoothiezView(TemplateView):
    template_name = 'zmoothiez.html'


class EthosView(TemplateView):
    template_name = 'ethos.html'


class ThirdView(TemplateView):
    template_name = '3rd.html'
