from django.test import TestCase
from django.test import Client
# Create your tests here.

class TestApplication(TestCase):

    def test_page_load(self):
        c = Client()
        response = c.get('/')
        self.assertEqual(response.status_code, 200)

