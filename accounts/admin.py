from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Profile

class ProfileInline(admin.StackedInline):
    """
    Inline admin configuration for Profile model.
    This allows editing profile fields directly in the User admin page.
    """
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fields = ['phone', 'address', 'date_of_birth']
    # Add more fields as needed

class CustomUserAdmin(UserAdmin):
    """
    Custom User admin to include Profile inline.
    This makes it easy to manage both user and profile data.
    """
    inlines = [ProfileInline]
    
    # Customize the list display
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff', 'is_superuser', 'is_active']
    list_filter = ['is_staff', 'is_superuser', 'is_active']
    
    # Add search fields
    search_fields = ['username', 'email', 'first_name', 'last_name']
    
    # Customize the fieldsets
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        ('Important Dates', {'fields': ('last_login', 'date_joined')}),
    )

# Re-register User admin
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

# Register Profile model separately (if needed)
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone', 'created_at']
    search_fields = ['user__username', 'user__email']