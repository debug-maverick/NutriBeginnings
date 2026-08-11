from django.urls import path
from . import views


urlpatterns = [

    # Home
    path(
        '',
        views.home,
        name='home'
    ),

    # Login
    path(
        'login/',
        views.login_view,
        name='login'
    ),

    # Register
    path(
        'register/',
        views.register_view,
        name='register'
    ),

    # Logout
    path(
        'logout/',
        views.logout_view,
        name='logout'
    ),

]