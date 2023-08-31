from django.core.mail import EmailMessage
from django.http import JsonResponse
from django.views.generic import TemplateView

from .mixins import ContactMixin
from .models import Banner


class HomeView(ContactMixin, TemplateView):
    template_name = 'index.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['banners'] = Banner.objects.filter(active=True)
        return context


class ContactView(ContactMixin, TemplateView):
    template_name = 'contact.html'

    def post(self, request, *args, **kwargs):
        email = EmailMessage(
            request.POST.get('subject'),
            request.POST.get('message'),
            to=['myemailaddress@gmail.com'],
            headers = {'FROM': request.POST.get('email')},
        )
        email.send()
        return JsonResponse({
            'detail': 'Ok'
        })
