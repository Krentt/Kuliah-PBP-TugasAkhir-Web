from django import http
from django.http import response
from django.test import TestCase
from django.test import Client
from django.urls import resolve
from .views import *
from django.contrib.auth.models import User
from .models import *
import time

# Create your tests here.

class CustomTest(TestCase):
    def test(self):
        user = User.objects.create_user(
            first_name="user",
            last_name="name",
            email="user@email.com",
            username="username",
            password="user_password",
        )
        self.client.login(username="username", password="user_password")
        response = self.client.get("/custom-mask/")
    
    def test_json(self):
        data = {'SURGICAL' : "Masker bedah atau bisa disebut sebagai masker medis yang biasanya berwarna hijau atau biru. Masker jenis ini mampu menahan droplet sekitar 80-90 persen. Masker ini hanya bisa digunakan satu kali pakai dalam waktu 4 jam pemakaian. Masker ini terutama wajib digunakan oleh pasien sakit dan petugas kesehatan yang tidak menangani pasien COVID-19 secara langsung. Petugas yang menangani pasien COVID-19 secara langsung wajib mengenakan masker N-95 dan APD level 3"}
        response = self.client.get('/data-deskripsi/', data)
        self.assertEqual(response.status_code, 200)

    def test_model(self):
        user1 = User.objects.create(username="ogiorgil", email="ogiorgil@localhost.com")
        obj1 = Order.objects.create(user=user1, complete=False, note='Sebuah Catatan')
        obj = CustomMask.objects.create(sex='M', size='M', model='SURGICAL', style='null', color='RED', price=10, quantity=11, order=obj1)
        self.assertEqual(obj.get_total(), 10*11)
