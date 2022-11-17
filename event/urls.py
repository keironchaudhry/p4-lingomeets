"""
URL patterns for 'event' app
"""

from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views

urlpatterns = [
    path(
        'past_meetups/',
        views.PastMeetups.as_view(),
        name='past_meetups'
    ),
    path(
        '<slug:slug>/',
        views.MeetupView.as_view(),
        name='meetup_detail'
    ),
    path(
        'register/<slug:slug>',
        login_required(views.AttendeeRegistration.as_view()),
        name='attendee_registration'
    ),
]
