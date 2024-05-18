from django.urls import reverse_lazy
from django.views.generic import TemplateView
from .models import AboutUs

class AboutUsView(TemplateView):
    template_name = 'aboutus.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about_us'] = AboutUs.objects.first()
        return context
