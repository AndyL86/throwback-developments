from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact, name='contact'),
    path('enquiry_confirm/', views.enquiry_confirm, name='enquiry_confirm'),
]
