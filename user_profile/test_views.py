from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import generic, View
from .forms import ProfileForm
from .models import Profile
from django.test import TestCase
from .models import Profile, User
import datetime


class TestProfileViews(TestCase):

    def setUp(self):
        """
        Creates a user object and 
        profile object for testing
        """
        User.objects.create_user(
            username='test_user',
            email='test_email@email.com',
            password='test_password'
        )
        test_profile = Profile.objects.create(
            user=User.objects.create_user(
                username='test_profile_user',
            ),
            first_name='Test First Name',
            last_name='Test Last Name',
            birthday=datetime.date.today(),
            native_language='Test Native Language',
            other_language='Test Other Language',
            bio='Test Bio',
            created_at=datetime.date.today(),
            updated_at=datetime.date.today()
        )

    def test_user_profile_returns_200(self):
        user = self.client.login(
            username='test_user',
            password='test_password'
        )
        response = self.client.get(
            '/user_profile/user_profile',
            follow=True
        )
        self.assertEqual(response.status_code, 200)

    def test_profile_view_dispatch(self):
        user = self.client.login(
            username='test_user',
            password='test_password'
        )
        self.client.post(
            f'/user_settings/',
            {'first_name': 'Test First Name'}
        )
        profile = Profile.objects.get(
            first_name='Test First Name'
        )
        self.assertEqual(profile.first_name, 'Test First Name')
        response = self.client.get(
            '/user_profile/user_profile/'
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user_profile.html')

    def test_profile_view_user_can_post(self):
        user = self.client.login(
            username='test_user',
            password='test_password'
        )
        profile = Profile.objects.get(
            bio='Test Bio'
        )
        self.client.post(
            f'/user_settings/',
            {'bio': 'Test Bio'}
        )
        self.assertEqual(profile.bio, 'Test Bio')
        response = self.client.get(
            '/user_profile/user_settings/'
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user_settings.html')
