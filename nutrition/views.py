from django.shortcuts import render, redirect, get_object_or_dict
from django.contrib.auth.decorators import login_required
from .models import FoodDiary, MealPlan, Payment

# 1. Main Landing / Index View
def index(request):
    """
    Renders the default home page for the nutrition module.
    """
    return render(request, 'nutrition/index.html')


# 2. Nutrition Dashboard (Requires Login)
@login_required
def nutrition_dashboard(request):
    """
    Fetches food entries, meal plans, and payment records for the logged-in user.
    """
    food_entries = FoodDiary.objects.filter(client=request.user).order_by('-date_logged')
    meal_plans = MealPlan.objects.filter(client=request.user).order_by('-created_at')
    payments = Payment.objects.filter(client=request.user).order_by('-payment_date')

    context = {
        'food_entries': food_entries,
        'meal_plans': meal_plans,
        'payments': payments,
    }
    return render(request, 'nutrition/dashboard.html', context)


# 3. Add Food Log Entry View
@login_required
def add_food_log(request):
    """
    Handles submitting a new food item entry into the diary.
    """
    if request.method == 'POST':
        food_item = request.POST.get('food_item')
        calories = request.POST.get('calories')
        meal_type = request.POST.get('meal_type')

        if food_item and calories and meal_type:
            FoodDiary.objects.create(
                client=request.user,
                food_item=food_item,
                calories=calories,
                meal_type=meal_type
            )
            return redirect('nutrition_dashboard')

    return render(request, 'nutrition/add_food.html')