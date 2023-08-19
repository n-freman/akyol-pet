from .forms import ContactForm


class ContactMixin:
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['contact_form'] = ContactForm()
        return context
