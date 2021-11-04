from django.test import TestCase
from django.test import Client
from django.urls import resolve
from .views import *
from .models import *

# Create your tests here.

class LoginTest(TestCase):

    def setUp(self) -> None:
        self.client = Client()

    def test_home_page_is_exist(self):
        response = self.client.get("/home-page")
        self.assertEqual(response.status_code, 200)

    def test_using_home_page_func(self):
        found = resolve("/home-page")
        self.assertEqual(found.func, home_page)