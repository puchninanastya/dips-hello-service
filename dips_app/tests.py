from django.test import TestCase

from django.test.client import RequestFactory

from . import views

class HelloTestCase(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()

    def test_hello_name(self):
        """hello view actually tells 'Hello, <name>!'."""
        # Setup.
        request = self.factory.get('/hello?name=Anastasia')
        # Run.
        response = views.hello(request)
        # Check.
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'<h1>Hello, Anastasia!</h1>')

    def test_hello_world(self):
        """Cannot find name, so tell 'Hello, world!'."""
        # Setup.
        request = self.factory.get('/hello')
        # Run.
        response = views.hello(request)
        # Check.
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'<h1>Hi!</h1>')
