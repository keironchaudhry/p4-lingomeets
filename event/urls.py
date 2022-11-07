"""
URL patterns for 'event' app
"""

from django.urls import path
from . import views

urlpatterns = [
    path('past_events/', views.PastEvents.as_view(), name='past_events')
]