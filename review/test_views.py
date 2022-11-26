from django.test import TestCase
from .models import Review, User
from event.models import Event
import datetime


class TestReviewViews(TestCase):

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

    def test_review_creation(self):
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
            content='Test content',
            rating=3
        )
        response = self.client.post(
            f'/event/{event.slug}/',
            {'content': 'Test content', 'rating': 3}
        )
        self.assertRedirects(
            response,
            f'/event/{event.slug}/'
        )

    def test_review_edit_view(self):
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
            content='Test content',
            rating=3
        )
        response = self.client.post(
            f'/event/{event.slug}/',
            {'content': 'Test content', 'rating': 3}
        )
        self.client.post(
            f'/review/edit/{review.id}',
            {'content': 'Edited Test content', 'rating': 5}
        )
        review = Review.objects.get(
            content='Edited Test content'
        )
        self.assertEqual(
            review.content,
            'Edited Test content'
        )
        self.assertEqual(
            review.rating,
            5
        )

    def test_user_can_delete_review(self):
        user = self.client.login(
            username='test_user',
            password='test_password'
        )
        event = Event.objects.get(
            title='Dummy Event title'
        )
        self.client.post(
            f'/event/{event.slug}/',
            {'content': 'Test content', 'rating': 3}
        )
        review = Review.objects.get(
            content='Test content'
        )
        self.assertEqual(
            review.content,
            'Test content'
        )
        response = self.client.post(
            f'/review/delete_review/{event.slug}'
        )
        self.assertRedirects(
            response,
            f'/event/{event.slug}/'
        )
        new_review = Review.objects.all()
        self.assertEqual(
            len(new_review),
            0
        )
