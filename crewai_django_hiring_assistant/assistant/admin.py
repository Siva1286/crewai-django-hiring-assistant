from django.contrib import admin
from .models import HiringGeneration

@admin.register(HiringGeneration)
class HiringGenerationAdmin(admin.ModelAdmin):
    list_display = ("job_title", "user", "experience_level", "created_at")
    list_filter = ("experience_level", "created_at")
    search_fields = ("job_title", "skills", "user__username")
    readonly_fields = ("created_at",)
