from django.views.generic import TemplateView


class DisclaimerView(TemplateView):
    template_name = 'disclaimer.html'
