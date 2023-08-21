from django import forms
from django.utils.translation import gettext_lazy as _


class ContactForm(forms.Form):
    email = forms.EmailField(label=_("Your email"))
    subject = forms.CharField(max_length=120, label=_("Subject"))
    message = forms.CharField(
        label=_("Message"),
        widget=forms.Textarea()
    )
