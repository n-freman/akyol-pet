from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from .views import HomeView, ContactView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contact', csrf_exempt(ContactView.as_view()), name='contact-us'),
]

