from django.urls import path
from . import views



urlpatterns = [
    # Redirect /accounts/ to login
    path('', views.home, name='home'),
    
    # Authentication
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),

    ]