from django.contrib import admin

from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'tech_stack', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('title', 'description', 'tech_stack')
