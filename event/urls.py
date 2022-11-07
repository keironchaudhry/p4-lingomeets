"""
URL patterns for 'event' app
"""

from django.urls import path
from . import views

urlpatterns = [
    path('past_meetups/', views.PastMeetups.as_view(), name='past_meetups'),
]
