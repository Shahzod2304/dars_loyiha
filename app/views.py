from django.shortcuts import render
from .models import *
# Create your views here.

def Home(request):
    homepage_elements = HomePage.objects.all()
    about = AboutCompany.objects.all()
    
    context = {
        'homepage_elements':homepage_elements,
        'about':about,
    }
    
    return render(request, 'index.html', context)


def About(request):
    return render(request, 'about.html')

def Contact(request):
    return render(request, 'contact.html')

def Guard(request):
    return render(request, 'guard.html')

def Service(request):
    return render(request, 'service.html')
