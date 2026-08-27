from django.db import models
from django.conf import settings

# If you have a custom Client/User model in your project, settings.AUTH_USER_MODEL handles it cleanly.

class FoodDiary(models.Model):
    client = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='food_diaries')
    food_item = models.CharField(max_length=200)
    calories = models.PositiveIntegerField()
    meal_type = models.CharField(
        max_length=50, 
        choices=[('Breakfast', 'Breakfast'), ('Lunch', 'Lunch'), ('Dinner', 'Dinner'), ('Snack', 'Snack')]
    )
    date_logged = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.client} - {self.food_item} ({self.meal_type})"


class MealPlan(models.Model):
    client = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='meal_plans')
    title = models.CharField(max_length=200)
    description = models.TextField()
    daily_calorie_target = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} for {self.client}"


class Payment(models.Model):
    client = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='payments')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(
        max_length=20, 
        choices=[('Pending', 'Pending'), ('Completed', 'Completed'), ('Failed', 'Failed')],
        default='Pending'
    )
    payment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.client} - {self.amount} ({self.status})"