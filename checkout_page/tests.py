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
        response = self.client.get("/checkout-1")
        self.assertEqual(response.status_code, 200)

    def test_using_checkout1_func(self):
        found = resolve("/checkout-1")
        self.assertEqual(found.func, checkout_form)

    def test_checkout2_is_exist(self):
        response = self.client.get("/checkout-2")
        self.assertEqual(response.status_code, 200)

    def test_using_checkout2_func(self):
        found = resolve("/checkout-2")
        self.assertEqual(found.func, checkout2_form)

    def test_checkout3_is_exist(self):
        response = self.client.get("/checkout-3")
        self.assertEqual(response.status_code, 200)

    def test_using_checkout3_func(self):
        found = resolve("/checkout-3")
        self.assertEqual(found.func, checkout3_form)

    def test_using_checkout4_func(self):
        found = resolve("/checkout-4")
        self.assertEqual(found.func, checkout4)

    def test_using_checkout_complete_func(self):
        found = resolve("/checkout-complete")
        self.assertEqual(found.func, checkout_complete)

    def test_valid_1(self):
        dictio = {"name": "Ini Nama", "email": "Ini@mail.com", "telp":"08522", "alamat":"Ini alamat"}
        response = self.client.post('/checkout-1', dictio)
        self.assertEqual(response.status_code, 302)

    def test_valid_2(self):
        dictio = {"durasi": "Next Day (1 hari) *Rp 10.000", "kurir": "AnterAja"}
        response = self.client.post('/checkout-2', dictio)
        self.assertEqual(response.status_code, 302)

    def test_valid_3(self):
        dictio = {"metode": "Mandiri Virtual Account"}
        response = self.client.post('/checkout-3', dictio)
        self.assertEqual(response.status_code, 302)

    def test_valid_4(self):
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
        self.assertEqual(response.status_code, 200)

    def test_valid_5(self):
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
        self.assertEqual(response.status_code, 200)
