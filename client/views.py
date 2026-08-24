#from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse
from .models import Client  # If you have a Client model

# Home page view
def home(request):
    context = {
        'page_title': 'Welcome to NutriBeginnings',
        'active_page': 'home'
    }
    return render(request, 'client/home.html', context)

# About page view
def about(request):
    context = {
        'page_title': 'About Us - NutriBeginnings',
        'active_page': 'about'
    }
    return render(request, 'client/about.html', context)

# Contact page view
def contact(request):
    context = {
        'page_title': 'Contact Us - NutriBeginnings',
        'active_page': 'contact'
    }
    return render(request, 'client/contact.html', context)

# Blogs page view (using progress_blog app)
def blogs(request):
    context = {
        'page_title': 'Blogs - NutriBeginnings',
        'active_page': 'blogs'
    }
    return render(request, 'client/blogs.html', context)

# Book Consultation page view
def book_consultation(request):
    context = {
        'page_title': 'Book Consultation - NutriBeginnings',
        'active_page': 'book_consultation'
    }
    return render(request, 'client/book_consultation.html', context)