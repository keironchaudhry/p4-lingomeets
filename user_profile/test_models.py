from .models import Profile
from django.test import TestCase
from .models import Profile, User
from datetime import date
import datetime


class TestProfileModel(TestCase):

    def setUp(self):
        """
        Creates a user object and
        profile object for testing
        """
        user = User.objects.create_user(
            username='test_user',
            email='test_email@email.com',
            password='test_password'
        )
        test_profile = Profile.objects.create(
            user=user,
            first_name='Test First Name',
            last_name='Test Last Name',
            birthday=datetime.date.today(),
            native_language='Test Native Language',
            other_language='Test Other Language',
            bio='Test Bio',
            created_at=datetime.date.today(),
            updated_at=datetime.date.today()
        )

    def test_profile_model_string_method_returns_string(self):
        profile = Profile.objects.get_or_create(
            first_name='Test First Name',
            last_name='Test Last Name'
        )
        self.assertEqual(
            str(profile),
            f'{profile}'
        )

    def test_age_method_returns_age(self):
        profile = Profile.objects.get(
            birthday=datetime.date.today(),
        )
        self.assertEqual(
            profile.birthday,
            datetime.date.today()
        )
        self.assertTrue(
            profile.birthday
        )
        today = date.today()
        self.assertEqual(
            today,
            date.today()
        )
        age = today.year - profile.birthday.year - (
            (
                today.month,
                today.day
            ) < (
                profile.birthday.month,
                profile.birthday.day
            )
        )
        self.assertEqual(
            age,
            0
        )
