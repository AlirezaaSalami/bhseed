from django.contrib import messages
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from .forms import ContactForm
from .models import ContactInfo


class ContactUsView(FormView):
    template_name = 'contactus.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact_us')

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Your message has been sent successfully.')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact_infos'] = ContactInfo.objects.all()
        return context
