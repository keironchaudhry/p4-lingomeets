from django.test import TestCase


class TestHomePage(TestCase):

    def test_home_page_returns_200(self):
        response = self.client.get(
            '/'
        )
        self.assertEqual(
            response.status_code,
            200
        )
        self.assertTemplateUsed(
            response,
            'index.html'
        )
