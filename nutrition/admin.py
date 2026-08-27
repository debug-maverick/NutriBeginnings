from django.contrib import admin
from .models import FoodDiary, MealPlan, Payment

@admin.register(FoodDiary)
class FoodDiaryAdmin(admin.ModelAdmin):
    list_display = ('client', 'food_item', 'calories', 'meal_type', 'date_logged')
    list_filter = ('meal_type', 'date_logged')
    search_fields = ('food_item', 'client__username')

@admin.register(MealPlan)
class MealPlanAdmin(admin.ModelAdmin):
    list_display = ('title', 'client', 'daily_calorie_target', 'created_at')
    search_fields = ('title', 'client__username')

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('client', 'amount', 'status', 'payment_date')
    list_filter = ('status', 'payment_date')
    search_fields = ('client__username',)