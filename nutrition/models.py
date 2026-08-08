from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class FoodDiary(models.Model):
    client = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='nutrition_food_diaries'
    )
    date = models.DateField(auto_now_add=True)
    meals_logged = models.TextField()
    calories = models.IntegerField(default=0)

    def __str__(self):
        return f"Food Diary for {self.client.username} on {self.date}"


class MealPlan(models.Model):
    client = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='nutrition_meal_plans'
    )
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.client.username}"


class Payment(models.Model):
    client = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='nutrition_payments'
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, default='Pending')

    def __str__(self):
        return f"Payment of {self.amount} by {self.client.username}"