from django.contrib import admin
from .models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    """
    Admin control for review model
    featured in Lingomeets website
    """
    list_display = ('event', 'user', 'rating', 'created_at')
    list_filter = ('event', 'user', 'rating', 'created_at')
    search_fields = ('user', 'event', 'rating')
