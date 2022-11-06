from django.test import TestCase
from . import views
from django.urls import reverse
from django.test.client import RequestFactory


# Create your tests here.


class DummyTestCase(TestCase):

    def test_dummy_test_case(self):
        self.assertEqual(1, 1)


class GoogleTests(TestCase):

    def test_connectGoogleLogin(self):
        response = self.client.get('http://127.0.0.1:8000/accounts/google/login/')
        self.assertEqual(200, response.status_code, response.content)

    def test_urls(self):
        url = reverse('depts', args=['acct'])
        self.assertEqual(url, '/acct')

        url = reverse('depts', args=['wgs'])
        self.assertEqual(url, '/wgs')

    def test_other_urls(self):
        url = reverse('depts', args=['cs'])
        self.assertEqual(url, '/cs')


class ViewTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_departments(self):
        request = self.factory.get('/acct')
        response = views.departments(request, 'acct')
        self.assertEqual(response.status_code, 200)

    def test_home(self):
        request = self.factory.get('')
        response = views.home(request)
        self.assertEqual(response.status_code, 200)
