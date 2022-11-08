from django.test import TestCase
from .models import Event, User
import datetime


class TestEventViews(TestCase):

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

    def test_past_meetups_page_returns_200(self):
        response = self.client.get('/event/past_meetups/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'past_meetups.html')

    def test_meetup_view_get_method(self):
        event = Event.objects.get(slug='dummy-event-title')
        response = self.client.get(f'/event/{event.slug}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'meetup_detail.html')
