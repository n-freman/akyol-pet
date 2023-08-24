from django.views.generic import DetailView, ListView

from .models import BottleCap, Preform


class PreformListView(ListView):
    model = Preform
    template_name = 'preforms/list.html'
    context_object_name = 'preforms'


class PreformDetailView(DetailView):
    model = Preform
    template_name = 'preforms/detail.html'
    context_object_name = 'preform'


class BottleCapListView(ListView):
    model = BottleCap
    template_name = 'bottlecaps/list.html'
    context_object_name = 'bottlecaps'


class BottleCapDetailView(DetailView):
    model = BottleCap
    template_name = 'bottlecaps/detail.html'
    context_object_name = 'bottlecap'
