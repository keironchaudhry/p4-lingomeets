from django.contrib import admin
from .models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    """
    Admin control for event model
    design feature for Lingomeets website
    """
    list_display = [
        'title',
        'slug',
        'created_on'
    ]
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = [
        'created_on'
    ]
