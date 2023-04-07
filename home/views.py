from django.shortcuts import render
from products.models import Product

# Create your views here.


def index(request):
    """ A view to return the index page """
    products = Product.objects.all()
    featured_products = list(Product.objects.filter(featured=True).order_by(
        'featured'))[-4:-1][::-1]  # show 4 recently featured products
    context = {
        'products': products,
        'featured_products': featured_products,
    }

    return render(request, 'home/index.html', context)
