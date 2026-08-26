from django.contrib import admin
from .models import Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):

    list_display = [
        'message_id',
        'client',
        'subject',
        'is_replied',
        'created_at'
    ]

    search_fields = [
        'subject',
        'message',
        'client__user__username'
    ]

    list_filter = [
        'is_replied',
        'created_at'
    ]

    readonly_fields = [
        'message_id',
        'created_at'
    ]
