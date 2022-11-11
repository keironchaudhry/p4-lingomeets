from django.shortcuts import render
from django.views import generic
from .models import Profile


class UserProfile(generic.ListView):
    """
    View for displaying user profile
    """
    model = Profile
    queryset = Profile.objects.all()
    template_name = 'user_profile.html'
