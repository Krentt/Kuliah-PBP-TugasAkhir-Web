from django import http
from django.http import response
from django.test import TestCase
from django.test import Client
from django.urls import resolve
from .views import *
from django.contrib.auth.models import User
from .models import *
import time

class Test(TestCase):
    def test_testing_is_exist(self):
        response = Client().get('/testing/')
        self.assertEqual(response.status_code, 200)
