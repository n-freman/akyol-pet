from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from .views import AboutUsView, ContactView, HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contact', csrf_exempt(ContactView.as_view()), name='contact-us'),
    path('about-us', AboutUsView.as_view(), name='about-us'),
]
