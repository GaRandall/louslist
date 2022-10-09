from django.test import TestCase

# Create your tests here.

from django.test import TestCase
from django.test import client
from django.contrib.auth import get_user_model


# Create your tests here.

class GoogleTests(TestCase):

    def setUp(self):
        self.client = client()
        self.user = get_user_model().objects.create_user(username="asdfghjkl", password="qwertyuiop",
                                                         email="me@test.com")
        self.user.save()

    def test_loginSuccess(self):
        self.client.login(username="asdfghjkl", password="qwertyuiop")
