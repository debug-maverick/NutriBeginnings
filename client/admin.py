#from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Client

'''@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone', 'date_of_birth', 'created_at']
    search_fields = ['user__username', 'user__email', 'phone']
    list_filter = ['created_at']
    readonly_fields = ['created_at', 'updated_at']'''

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = [
        'client_id',
        'user',
        'phone',
        'age',
        'gender',
        'height',
        'weight',
        'goal',
        'created_at'
    ]

    search_fields = [
        'user__username',
        'user__email',
        'phone'
    ]

    list_filter = [
        'gender',
        'goal',
        'created_at'
    ]

    readonly_fields = [
        'created_at',
        'updated_at'
    ]