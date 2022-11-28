from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import generic, View
from .forms import ProfileForm
from .models import Profile


class UserProfile(generic.ListView):
    """
    View for displaying user
    profile featured in Lingomeets
    """
    model = Profile
    queryset = Profile.objects.all()
    template_name = 'user_profile.html'


# https://themesberg.com/blog/django/user-profile-tutorial
# The above source was useful guidance in creating a user profile
class UserSettings(View):
    """
    View for user settings used
    to modify user profile information
    """
    def dispatch(self, request, *args, **kwargs):
        self.profile, __ = Profile.objects.get_or_create(
            user=request.user
        )
        return super(UserSettings, self).dispatch(
            request,
            *args,
            **kwargs
        )

    def get(self, request):
        context = {
            'profile': self.profile
        }
        return render(
            request,
            'user_settings.html',
            context
        )

    def post(self, request):
        form = ProfileForm(
            request.POST,
            request.FILES,
            instance=self.profile
        )
        if form.is_valid():
            profile = form.save(commit=False)
            profile.save()

            messages.success(
                request,
                'Profile saved successfully.'
            )
        else:
            messages.error(
                request,
                'Please enter validate input.'
                )
        return redirect(
            'user_settings'
        )
