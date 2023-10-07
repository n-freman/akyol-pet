class PrevNextMixin:

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        if 'object' in kwargs.keys():
            context['prev'] = self.model.objects.filter(code__lt=kwargs['object'].code).last()
            context['next'] = self.model.objects.filter(code__gt=kwargs['object'].code).first()
        return context
