from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm


def contact(request):
    """ View to render contact form """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Send the email
            name = form.cleaned_data['name']
            from_email = form.cleaned_data['email']
            vehicle = form.cleaned_data['vehicle']
            enquiry = form.cleaned_data['enquiry']
            recipient = settings.DEFAULT_FROM_EMAIL
            subject = f'Throwback Developments enquiry form: {name}, {from_email}'
            send_mail(subject, message, from_email, [recipient])
            return redirect('enquiry_confirm')
    else:
        form = ContactForm()
    return render(request, 'contact/contact.html', {'form': form})


def enquiry_confirm(request):
    """ View to render enquiry confirmation notification """
    return render(request, 'contact/enquiry_confirm.html')
