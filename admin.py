from django.contrib import admin
from .models import Progress, Blog

@admin.register(Progress)
class ProgressAdmin(admin.ModelAdmin):
    list_display = ("date", "weight", "calories", "water", "steps")
    list_filter = ("date",)
    search_fields = ("notes",)

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "created_at", "updated_at")
    search_fields = ("title", "excerpt", "content", "author")
    prepopulated_fields = {"slug": ("title",)}
