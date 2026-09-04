from django.contrib import admin
from .models import FoodDiary, MealPlan, Payment

admin.site.register(FoodDiary)
admin.site.register(MealPlan)
admin.site.register(Payment)