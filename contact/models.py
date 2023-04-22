from django.db import models


class Contact(models.Model):
    """ Model for user contact form """
    # Set enquiry type for contact form
    ORDER = 'OR'
    PRODUCT = 'PR'
    CUSTOM = 'CU'
    TYPE_CHOICES = [
        ('', 'Select Type *'),
        (ORDER, 'Order Status'),
        (PRODUCT, 'Product Enquiry'),
        (CUSTOM, 'Custom Application Enquiry'),
    ]
    type = models.CharField(max_length=2, choices=TYPE_CHOICES)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    enquiry = models.TextField(max_length=1000)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        """ Ordering and plural name """
        ordering = ['-date_created']
        verbose_name_plural = 'Contact Us'

    def __str__(self):
        return f'Message from {self.name}'
