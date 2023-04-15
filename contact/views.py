from django.shortcuts import render, redirect
from django.contrib import messages

from django.core.mail import send_mail
from django.conf import settings

from django.template.loader import render_to_string

from .forms import ContactForm


def contact(request):
    """ View to render contact form """

    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()

            # Form submission confirmation
            type = form.cleaned_data['type']
            name = form.cleaned_data['name']
            original_enquiry = form.cleaned_data['enquiry']
            enquiry = render_to_string(
                'contact/confirmation_email/confirmation_email.txt', {
                    'name': name,
                    'original_enquiry': original_enquiry
                })
            email_from = settings.DEFAULT_FROM_EMAIL
            email_to = [form.cleaned_data['email']]

            send_mail(
                type,
                enquiry,
                email_from,
                email_to
            )

            messages.success(request, 'Message sent successfully \
                A confirmation email has been sent to your email')

    form = ContactForm

    context = {
        'form': form,
    }

    template = 'contact/contact.html'

    return render(request, template, context)


def enquiry_confirm(request):
    """ View to render enquiry confirmation notification """
    return render(request, 'contact/enquiry_confirm.html')
