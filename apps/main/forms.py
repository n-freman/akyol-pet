from django import forms


class ContactForm(forms.Form):
    email = forms.EmailField(label="Your email")
    subject = forms.CharField(max_length=120, label="Subject")
    message = forms.CharField(
        label="Message",
        widget=forms.Textarea()
    )
