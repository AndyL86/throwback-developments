from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    """
    Model for Product Categories. Credit Boutique Ado Walkthrough.
    """
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=300)
    friendly_name = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    """
    Model for the Products
    """
    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    title = models.CharField(max_length=254)
    make = models.CharField(max_length=254)
    model = models.CharField(max_length=254)
    variant = models.CharField(max_length=254)
    description = models.TextField()
    construction = models.CharField(max_length=254)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2,
                                 null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    featured = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.title


class ProductReview(models.Model):
    """
    Model for Product Reviews
    """
    product = models.ForeignKey(
        Product, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(
        User, related_name='reviews', on_delete=models.CASCADE)
    review = models.TextField(blank=True, null=True)
    stars = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)


class Wishlist(models.Model):
    """
    Model for users to add products to a wishlist
    """
    product = models.ForeignKey(
        Product, related_name='wishlist', on_delete=models.CASCADE)
    user = models.ForeignKey(
        User, related_name='wishlist', on_delete=models.CASCADE)

    def __str__(self):
        return self.product.title
