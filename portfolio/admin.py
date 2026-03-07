from django.contrib import admin

from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "created", "updated_at")
    search_fields = ("title", "description")
    readonly_fields = ("created", "updated_at")
