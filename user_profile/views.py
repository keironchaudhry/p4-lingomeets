from django.shortcuts import render
from django.contrib import messages
from django.views import generic, View
from .models import Profile


class UserProfile(generic.ListView):
    """
    View for displaying user profile
    """
    model = Profile
    queryset = Profile.objects.all()
    template_name = 'user_profile.html'


class UserSettings(View):
    """
    View for user settings used
    to modify user profile information
    """
    def get(self, request):
        self.profile = Profile.objects.get_or_create(user=request.user)
        context = {'profile': self.profile}
        return render(request, 'user_settings.html', context)

    def post(self, request):
        form = ProfileForm(request.POST, request.FILES, instance=self.profile)

        if form.is_valid():
            profile = form.save(commit=False)
            profile.save()

            messages.success(request, 'Profile saved successfully')
        else:
            messages.error(
                request,
                'Profile could not be updated. Please contact admin.'
                )
        return redirect('user_profile')
