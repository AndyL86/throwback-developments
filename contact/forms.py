from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label='Full name', max_length=100)
    email = forms.EmailField(label='Your Email')
    vehicle = forms.CharField(label='Vehicle Details', max_length=100)
    enquiry = forms.CharField(widget=forms.Textarea)
