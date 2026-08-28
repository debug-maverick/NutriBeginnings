# Register your models here.
from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

    list_display = (
        'user',
        'phone',
        'gender',
        'current_weight',
        'goal_weight',
        'fitness_goal',
        'created_at',
    )

    search_fields = (
        'user__username',
        'user__first_name',
        'user__last_name',
        'phone',
    )

    list_filter = (
        'gender',
        'fitness_goal',
        'created_at',
    )