from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

    list_display = (
        'user',
        'first_name',
        'last_name',
        'birthday',
        'native_language',
        'other_language',
        'bio',
        'created_at',
        'updated_at'
    )
    list_filter = (
        'user',
        'birthday',
        'native_language',
        'other_language',
        'created_at',
        'updated_at'
    )
    search_fields = (
        'user',
        'native_language',
        'other_language'
    )
