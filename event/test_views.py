from django.test import TestCase


class TestEventViews(TestCase):

    def test_past_meetups_page_returns_200(self):
        response = self.client.get('/event/past_meetups/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'past_meetups.html')
