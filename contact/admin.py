from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """ Contact management section for admin """
    list_display = ['name', 'type']
