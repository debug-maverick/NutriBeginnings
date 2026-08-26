#from django.shortcuts import render

# Create your views here.
from .models import Profile, Message
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


from client.forms import MessageForm

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
@login_required
def contact(request):

    form = MessageForm()

    return render(request, 'client/contact.html', {
        'form': form,
        'page_title': 'Contact Us - NutriBeginnings',
        'active_page': 'contact'
    })

@login_required
def send_message(request):

    profile = Profile.objects.get(user=request.user)

    if request.method == 'POST':

        form = MessageForm(request.POST)

        if form.is_valid():

            message = form.save(commit=False)

            message.client = profile

            message.save()

            return redirect('client:message_success')

    else:

        form = MessageForm()

    return render(request, 'client/contact.html', {
        'form': form
    })


@login_required
def message_success(request):
    return render(request, 'client/message_success.html')

# Blogs page view (using progress_blog app)
def blogs(request):

    if request.method == 'POST':

        form = MessageForm(request.POST)

        if form.is_valid():
            # Process the form data (e.g., save to database, send email, etc.)
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # You can add your logic here to handle the form submission

            # Redirect to a success page or render a success message
            return HttpResponse("Thank you for your message!")

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