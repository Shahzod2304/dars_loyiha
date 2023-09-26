from django.urls import path 
from .views import * 

urlpatterns = [
    path('', Home, name='home'),
    path('about/', About, name='about'),
    path('contact/', Contact, name="contact"),
    path('guard/', Guard, name='guards'),
    path('service/', Service, name='service'),
]
