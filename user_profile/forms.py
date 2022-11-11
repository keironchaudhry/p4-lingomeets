from .models import Profile
from django import forms


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = (
            'user',
            'first_name',
            'last_name',
            'birthday',
            'avatar',
            'native_language',
            'other_language',
            'bio'
        )
        exclude = ['user']
