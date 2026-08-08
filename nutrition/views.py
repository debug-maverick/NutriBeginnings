import uuid
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Recipe, MealPlan, FoodDiary, Payment

# --- MEAL PLAN & PAYMENT VIEWS ---

@login_required
def meal_plan_list(request):
    """Lists all meal plans assigned to the logged-in client."""
    plans = MealPlan.objects.filter(client=request.user)
    return render(request, 'nutrition/meal_plan_list.html', {'plans': plans})

@login_required
def meal_plan_detail(request, plan_id):
    """Displays meal plan details if paid; otherwise prompts payment."""
    plan = get_object_or_404(MealPlan, id=plan_id, client=request.user)
    
    if not plan.is_paid:
        return render(request, 'nutrition/payment_required.html', {'plan': plan})
    
    return render(request, 'nutrition/meal_plan_detail.html', {'plan': plan})

@login_required
def process_payment(request, plan_id):
    """Handles the simulated payment process to unlock the meal plan."""
    plan = get_object_or_404(MealPlan, id=plan_id, client=request.user)
    
    if plan.is_paid:
        return redirect('meal_plan_detail', plan_id=plan.id)

    if request.method == "POST":
        # Simulate successful transaction
        txn_id = f"TXN-{uuid.uuid4().hex[:10].upper()}"
        
        Payment.objects.create(
            client=request.user,
            meal_plan=plan,
            amount=plan.price,
            transaction_id=txn_id,
            status='Completed'
        )
        
        plan.is_paid = True
        plan.save()
        
        messages.success(request, "Payment successful! Your customized meal plan is unlocked.")
        return redirect('meal_plan_detail', plan_id=plan.id)

    return render(request, 'nutrition/checkout.html', {'plan': plan})


# --- RECIPE VIEWS ---

def recipe_list(request):
    """Lists all available recipes."""
    recipes = Recipe.objects.all()
    return render(request, 'nutrition/recipe_list.html', {'recipes': recipes})

def recipe_detail(request, recipe_id):
    """Displays single recipe details."""
    recipe = get_object_or_404(Recipe, id=recipe_id)
    return render(request, 'nutrition/recipe_detail.html', {'recipe': recipe})


# --- FOOD DIARY VIEWS ---

@login_required
def food_diary_list(request):
    """Displays the logged-in client's food diary entries."""
    entries = FoodDiary.objects.filter(client=request.user).order_by('-date')
    return render(request, 'nutrition/food_diary.html', {'entries': entries})

@login_required
def add_food_diary(request):
    """Allows client to log meals."""
    if request.method == "POST":
        meal_type = request.POST.get('meal_type')
        food_item = request.POST.get('food_item')
        calories = request.POST.get('calories')
        notes = request.POST.get('notes')

        FoodDiary.objects.create(
            client=request.user,
            meal_type=meal_type,
            food_item=food_item,
            calories=calories if calories else None,
            notes=notes
        )
        messages.success(request, "Food entry logged successfully!")
        return redirect('food_diary_list')

    return render(request, 'nutrition/add_food_diary.html')