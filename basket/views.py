from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404)
from django.contrib import messages

from products.models import Product


def view_basket(request):
    """ A view that renders the basket contents page """

    return render(request, 'basket/basket.html')


def add_to_basket(request, item_id):
    """ Add a quantity of a product to the shopping basket """

    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))

    if quantity > 99:
        quantity = 99
        messages.error(request, f'Sorry, you can only add 99/n
                       of {product.title} to your basket')
    elif quantity < 1:
        quantity = 1
        messages.error(request, f'Sorry, you must add at least/n
                       1 of {product.title} to your basket')

    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    if item_id in list(basket.keys()):
        basket[item_id] += quantity
    else:
        basket[item_id] = quantity
        messages.success(request, f'Added {product.title} to your basket')

    request.session['basket'] = basket
    return redirect(redirect_url)


def edit_basket(request, item_id):
    """ Edit a quantity of a product in the shopping basket """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    basket = request.session.get('basket', {})

    if quantity > 0:
        basket[item_id] = quantity
        messages.success(request, f'Updated {product.title}/n
                         quantity {basket[item_id]}')
    else:
        basket.pop(item_id)
        messages.success(request, f'Removed {product.title} from your basket')

    request.session['basket'] = basket
    return redirect(reverse('view_basket'))


def remove_item(request, item_id):
    """ Remove product from basket """
    product = get_object_or_404(Product, pk=item_id)
    basket = request.session.get('basket', {})
    quantity = basket[item_id] - 10

    if quantity > 0:
        basket[item_id] = quantity
    else:
        basket.pop(item_id)
        messages.success(request, f'Removed {product.title} from your basket')

    request.session['basket'] = basket
    if not basket:
        return redirect(reverse('view_basket'))
    return redirect(reverse('view_basket'))
