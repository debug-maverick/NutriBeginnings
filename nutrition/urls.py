from django.urls import path
from . import views

urlpatterns = [
    # Match this view name to whatever function exists in your nutrition/views.py
    path('', views.index, name='nutrition_index'), 
]