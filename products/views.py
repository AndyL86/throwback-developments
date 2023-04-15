from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from django.contrib.auth.models import User
from .models import Product, Category, ProductReview, Wishlist
from .forms import ProductForm, ReviewForm


def all_products(request):
    """ View to show individual product details """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category_id'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Please enter a search criteria")
                return redirect(reverse('products'))

            queries = Q(title__icontains=query) | Q(
                description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_details(request, product_id):
    """ View to show all  products, including sorting and  search queries """

    product = get_object_or_404(Product, pk=product_id)
    form = ReviewForm()
    user = request.user

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.product = product
            review = form.save()
            messages.success(request, 'Successfully added review!')
            return redirect(reverse('product_details', args=[product.id]))
        else:
            messages.error(request, 'Failed to add review.\
                 Please check that the form is valid.')

    context = {
        'product': product,
        'form': form,
    }

    return render(request, 'products/product_details.html', context)


@login_required
def add_product(request):
    """ View for adding a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Only Administrators have those permissions.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Product added successfully!')
            return redirect(reverse('product_details', args=[product.id]))
        else:
            messages.error(request, '''An error occured, please check your
                           form is correct and try again!''')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ View for updating a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Only Administrators have those permissions.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product updated successfully!')
            return redirect(reverse('product_details', args=[product_id]))
        else:
            messages.error(request, '''An error occured, please check your
                           form is correct and try again!''')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are updating {product.title}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ View for deleting a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Only Administrators have those permissions.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product removed successfully!')
    return redirect(reverse('products'))


@login_required
def add_to_wishlist(request, product_id, user_id):
    """ View for adding a product to wishlist """
    product = Product.objects.get(id=product_id)
    user = User.objects.get(id=user_id)
    wishlist_item, created = Wishlist.objects.get_or_create(
        product=product, user=user)
    if created:
        wishlist_item.save()
        messages.success(request, 'Product added to your wishlist')
    else:
        messages.info(request, 'Product is already in your wishlist')

    return redirect(reverse('product_details', args=[product_id]))


@login_required
def wishlist(request):
    """ View for user wishlist """
    user = request.user
    wishlist = Wishlist.objects.filter(user=user)
    context = {
        'wishlist': wishlist,
    }
    template = 'products/wishlist.html'

    return render(request, template, context)


@login_required
def remove_from_wishlist(request, wishlist_id):
    """ View for removing products from wishlist """
    wishlist_item = Wishlist.objects.get(id=wishlist_id)

    wishlist_item.delete()
    messages.success(request, 'Product removed from wishlist')
    referer = request.META.get('HTTP_REFERER')
    if referer:
        if 'wishlist' in referer:
            return redirect('wishlist')
        else:
            return redirect(referer)
    else:
        return redirect('wishlist')
