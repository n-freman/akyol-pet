from django.views.generic import TemplateView
from django.http import JsonResponse
from django.core.mail import EmailMessage
from django.conf import settings

from .mixins import ContactMixin


class HomeView(ContactMixin, TemplateView):
    template_name = 'index.html'



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
