import datetime
from django.test import TestCase
from .models import User, Event


class TestEventModel(TestCase):

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

    def test_event_model_string_method_returns_string(self):
        event = Event.objects.get(
            title='Dummy Event title'
        )
        self.assertEqual(
            str(event),
            'Dummy Event title'
        )
