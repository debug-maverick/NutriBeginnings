from django.db import models
from django.contrib.auth.models import User

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    ingredients = models.TextField()
    instructions = models.TextField()
    calories = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class MealPlan(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='meal_plans')
    title = models.CharField(max_length=200)
    description = models.TextField()
    plan_details = models.TextField(help_text="Detailed meal plan instructions")
    price = models.DecimalField(max_digits=8, decimal_places=2, default=499.00)
    is_paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.client.username}"

class FoodDiary(models.Model):
    MEAL_CHOICES = [
        ('Breakfast', 'Breakfast'),
        ('Lunch', 'Lunch'),
        ('Dinner', 'Dinner'),
        ('Snack', 'Snack'),
    ]
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='food_diaries')
    date = models.DateField(auto_now_add=True)
    meal_type = models.CharField(max_length=20, choices=MEAL_CHOICES)
    food_item = models.CharField(max_length=200)
    calories = models.IntegerField(null=True, blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.client.username} - {self.meal_type} ({self.date})"

class Payment(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    meal_plan = models.OneToOneField(MealPlan, on_delete=models.CASCADE, related_name='payment')
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    transaction_id = models.CharField(max_length=100, unique=True)
    status = models.CharField(max_length=20, default='Completed')
    payment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment {self.transaction_id} by {self.client.username}"