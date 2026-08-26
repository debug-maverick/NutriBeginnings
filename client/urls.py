from django.urls import path
from . import views

app_name = 'client'

urlpatterns = [
    # Home page
    path('', views.home, name='home'),
    
    # About page
    path('about/', views.about, name='about'),
    
    # Contact page
    path('contact/', views.contact, name='contact'),
    path('send-message/', views.send_message, name='send_message'),
    path('message-success/', views.message_success, name='message_success'),
    
    # Blogs page
    path('blogs/', views.blogs, name='blogs'),
    
    # Book Consultation page
    path('book-consultation/', views.book_consultation, name='book_consultation'),

]