from django.test import TestCase

# Create your tests here.

class GoogleTests(TestCase):

    def test_connectGoogleLogin(self):
        response = self.client.get('http://127.0.0.1:8000/accounts/google/login/')
        self.assertEqual(200, response.status_code, response.content)