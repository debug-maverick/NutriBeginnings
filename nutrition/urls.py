from django.urls import path
from . import views

urlpatterns = [
    # Main page for your nutrition app
    path('', views.index, name='nutrition_index'),
    
    # Add any extra views you create here, e.g.:
    # path('dashboard/', views.nutrition_dashboard, name='nutrition_dashboard'),
]