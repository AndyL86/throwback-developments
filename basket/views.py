from django.shortcuts import render, redirect, reverse, HttpResponse


def view_basket(request):
    """ A view that renders the basket contents page """

    return render(request, 'basket/basket.html')


def add_to_basket(request, item_id):
    """ Add a quantity of a product to the shopping basket """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    if item_id in list(basket.keys()):
        basket[item_id] += quantity
    else:
        basket[item_id] = quantity

    request.session['basket'] = basket
    return redirect(redirect_url)


def edit_basket(request, item_id):
    """ Edit a quantity of a product in the shopping basket """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    basket = request.session.get('basket', {})

    if quantity > 0:
        basket[item_id] = quantity
    else:
        basket.pop(item_id)

    request.session['basket'] = basket
    return redirect(reverse('view_basket'))

def remove_item(request, item_id):
    """
    Remove entire quantity of a given product.
    """
    product = get_object_or_404(Product, pk=item_id)
    basket = request.session.get('basket', {})
    quantity = basket[item_id] - 10

    if quantity > 0:
        basket[item_id] = quantity
    else:
        basket.pop(item_id)

    request.session['basket'] = basket
    if not basket:
        return redirect(reverse('basket'))
    return redirect(reverse('basket'))