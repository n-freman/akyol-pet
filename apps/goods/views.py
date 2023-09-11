from django.utils.translation import get_language
from django.views.generic import DetailView, ListView

from .models import BottleCap, Preform
from .mixins import PrevNextMixin


class PreformListView(ListView):
    model = Preform
    template_name = 'preforms/list.html'
    context_object_name = 'preforms'


class PreformDetailView(PrevNextMixin, DetailView):
    model = Preform
    template_name = 'preforms/detail.html'
    context_object_name = 'preform'


class BottleCapListView(ListView):
    model = BottleCap
    template_name = 'bottlecaps/list.html'
    context_object_name = 'bottlecaps'

    def get_queryset(self):
        return self.model.objects.all() \
            .translate(lang=get_language())


class BottleCapDetailView(PrevNextMixin, DetailView):
    model = BottleCap
    template_name = 'bottlecaps/detail.html'
    context_object_name = 'bottlecap'

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()

        # Next, try looking up by primary key.
        pk = self.kwargs.get(self.pk_url_kwarg)
        queryset = queryset.filter(pk=pk) \
            .translate(lang=get_language())
        return queryset.first()
