from django.test import TestCase
from .models import Review, User
from event.models import Event
import datetime


class TestReviewModel(TestCase):

    def setUp(self):
        """
        setUp method which creates a test event object
        """
        test_event = Event.objects.create(
            title='Dummy Event title',
            slug='dummy-event-title',
            date=datetime.date.today(),
            destination='Dummy Event Destination',
            description='Dummy description of Event',
            price=0,
        )
        test_event.attendees.set([])
        User.objects.create_user(
            username='test_user',
            email='test_email@email.com',
            password='test_password'
        )

    def test_review_model_method_returns_string(self):
        self.client.login(
            username='test_user',
            password='test_password'
        )
        event = Event.objects.get(
            title='Dummy Event title'
        )
        user = User.objects.get(
            username='test_user'
        )
        review = Review.objects.create(
            event=event,
            user=user,
            content='Test content'
        )
        self.assertEqual(
            str(review), 'Review: Test content by test_user'
        )
