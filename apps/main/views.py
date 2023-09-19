from typing import Any

from django.core.mail import EmailMessage
from django.http import JsonResponse
from django.utils.translation import get_language
from django.views.generic import TemplateView

from .forms import ContactForm
from .mixins import ContactMixin
from .models import AboutPage, Banner, FeedBack


class HomeView(ContactMixin, TemplateView):
    template_name = 'index.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['banners'] = Banner.objects.filter(active=True)\
            .translate(lang=get_language())
        return context


class ContactView(ContactMixin, TemplateView):
    template_name = 'contact.html'

    def post(self, request, *args, **kwargs):
        # email = EmailMessage(
        #     request.POST.get('subject'),
        #     request.POST.get('message'),
        #     to=['myemailaddress@gmail.com'],
        #     headers = {'FROM': request.POST.get('email')},
        # )
        # email.send()
        form = ContactForm(request.POST)
        if form.is_valid():
            FeedBack.objects.create(
                **form.cleaned_data
            )
            return JsonResponse({
                'detail': 'Ok'
            })
        print(form.errors)
        return JsonResponse(
            {
                'detail': 'Error'
            },
            status=400,
        )


class AboutUsView(TemplateView):
    template_name = 'about_us.html'

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        try:
            context['page'] = AboutPage.objects.first()
        except Exception as e:
            print(e)
            context['page'] = None
        return context
