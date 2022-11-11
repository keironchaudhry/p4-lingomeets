from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views

urlpatterns = [
    path(
        'user_profile/',
        login_required(views.UserProfile.as_view()),
        name='user_profile'
    ),
]