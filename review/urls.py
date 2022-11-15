"""
URL patterns for 'review' app
"""

from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views

urlpatterns = [
    path(
        'edit/<pk>',
        login_required(views.EditReview.as_view()),
        name='edit_review'
    ),
    path(
        'delete_review/<slug:slug>',
        login_required(views.DeleteReview.as_view()),
        name='delete_review'
    ),
]
