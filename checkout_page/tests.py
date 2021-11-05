from django.http import response
from django.test import TestCase
from django.test import Client
from django.urls import resolve
from .views import *
from django.contrib.auth.models import User
from .models import *
import time

# Create your tests here.

class CheckoutTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_checkout1_is_exist(self):
        user = User.objects.create_user(
            first_name="user",
            last_name="name",
            email="user@email.com",
            username="username",
            password="user_password",
        )
        self.client.login(username="username", password="user_password")
        response = self.client.get("/checkout-1")
        self.assertEqual(response.status_code, 302)

        data = {"name": "Ini Nama", "email": "Ini@mail.com", "telp":"", "alamat":"Ini alamat"}
        response = self.client.post('/checkout-1', data)
        self.assertEqual(response.status_code, 200)

    def test_checkout2_is_exist(self):
        user = User.objects.create_user(
            first_name="user",
            last_name="name",
            email="user@email.com",
            username="username",
            password="user_password",
        )
        self.client.login(username="username", password="user_password")
        response = self.client.get("/checkout-2")
        self.assertEqual(response.status_code, 302)

        data = {"durasi": "Next Day (1 hari)", "kurir": "AnterAja"}
        response = self.client.post('/checkout-2', data)
        self.assertEqual(response.status_code, 302)

    def test_checkout3_is_exist(self):
        user = User.objects.create_user(
            first_name="user",
            last_name="name",
            email="user@email.com",
            username="username",
            password="user_password",
        )
        self.client.login(username="username", password="user_password")
        response = self.client.get("/checkout-3")
        self.assertEqual(response.status_code, 302)

    def test_checkout4_is_exist(self):
        dictio1 = {"name": "Ini Nama", "email": "Ini@mail.com", "telp":"08522", "alamat":"Ini alamat"}
        dictio2 = {"durasi": "Next Day (1 hari) *Rp 10.000", "kurir": "AnterAja"}
        dictio3 = {"metode": "Mandiri Virtual Account"}
        user = User.objects.create_user(
            first_name="user",
            last_name="name",
            email="user@email.com",
            username="username",
            password="user_password",
        )
        self.client.login(username="username", password="user_password")
        order, created = Order.objects.get_or_create(user=user, complete=False)
        data = {'checkouts': dictio1,'pengirimans': dictio2, 'pembayarans': dictio3, 'user':user, 'order':order}
        response = self.client.post('/checkout-4', data)
        self.assertEqual(response.status_code, 302)

    def test_checkout_complete_is_exist(self):
        dictio1 = {}
        dictio2 = {}
        dictio3 = {}
        user = User.objects.create_user(
            first_name="user",
            last_name="name",
            email="user@email.com",
            username="username",
            password="user_password",
        )
        self.client.login(username="username", password="user_password")
        order, created = Order.objects.get_or_create(user=user, complete=True)
        data = {'checkouts': dictio1,'pengirimans': dictio2, 'pembayarans': dictio3, 'user':user, 'order':order}
        response = self.client.post('/checkout-complete', data)
        self.assertEqual(response.status_code, 302)
