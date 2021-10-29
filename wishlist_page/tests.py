from django.test import TestCase
from django.test import Client
from django.urls import resolve
from .views import *
from django.http import HttpRequest
import factory
from factory.django import DjangoModelFactory
from django.contrib.auth.models import User
from .models import WishlistItem

class UserFactory(DjangoModelFactory):

    username = factory.Sequence('testuser{}'.format)
    email = factory.Sequence('testuser{}@company.com'.format)

    class Meta:
        model = User


# Create your tests here.

class WishlistTest(TestCase):
    def test_wishlist_is_exist(self):
        response = Client().get("/wishlist/")
        self.assertEqual(response.status_code, 200)

    def test_using_index_func(self):
        found = resolve("/wishlist/")
        self.assertEqual(found.func, index)
    
    def test_attributes(self):
        user1 = UserFactory(username="ogiorgil", email="ogiorgil@localhost.com")
        WishlistItem.objects.create(owner=user1, name="one", price=1 , count=1)
        obj1 = WishlistItem.objects.get(owner=user1)
        self.assertEqual(obj1.name, "one")
        self.assertEqual(obj1.price, 1)
        self.assertEqual(obj1.count, 1)
    

     