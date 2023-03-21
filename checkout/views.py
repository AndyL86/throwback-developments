from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, "There's nothing in your basket at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51MbQDcF3fnFFVBJeI0c06HLWHVPW5oBafoGMO86HupjvqwtdcC3OCypWY2PdYqMEY1SUnYXTb1Ihu3cc8u5TC9fo00DN9n17Yv'
    }

    return render(request, template, context)