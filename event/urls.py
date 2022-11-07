"""
URL patterns for 'event' app
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home')
]