from django.test import TestCase


class Basic(TestCase):
    def test_basic(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 404)
