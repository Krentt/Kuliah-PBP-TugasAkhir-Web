from django.http import response
from django.test import TestCase
from django.test import Client
from django.urls import resolve
from .views import *
from django.contrib.auth.models import User
from .models import *
import time

# Create your tests here.

class ShoppingCartTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_cart_text_in_html_not_login(self):
        response = Client().get('/cart/')
        html_response = response.content.decode('utf8')
        self.assertIn("Please login or register to view your cart", html_response)

    def test_cart_text_in_html_login(self):
        User.objects.create_user(
            first_name="user",
            last_name="name",
            email="user@email.com",
            username="username",
            password="user_password",
        )

        self.client.login(username="username", password="user_password")
        response = self.client.get('/cart/')
        html_response = response.content.decode('utf8')
        self.assertIn("0", html_response)

    def test_order_attributes(self):
        user1 = User.objects.create(username="ogiorgil", email="ogiorgil@localhost.com")
        obj1 = Order.objects.create(user=user1, complete=False, note='Sebuah Catatan')
        orderitems = obj1.orderitem_set.all()
        customitems = obj1.custommask_set.all()

        self.assertEqual(obj1.user, User.objects.get(username='ogiorgil'))
        self.assertEqual(obj1.complete, False)
        self.assertEqual(obj1.note, 'Sebuah Catatan')

        total = sum([item.get_total() for item in orderitems])
        totalcustom = sum([item.get_total() for item in customitems])
        self.assertEqual(obj1.get_price_total(), total+totalcustom)

        total = sum([item.quantity for item in orderitems])
        totalcustom = sum([item.quantity for item in customitems])
        self.assertEqual(obj1.get_items_total(), total+totalcustom)
    
    def test_orderitem_attributes(self):
        user1 = User.objects.create(username="ogiorgil", email="ogiorgil@localhost.com")
        product1 = ProdukMasker.objects.create(nama='Masker kain', rating=100, deskripsi='Masker berkualitas', stok='100', harga='10')
        order1 = Order.objects.create(user=user1, complete=False, note='Sebuah Catatan')
        obj1 = OrderItem.objects.create(product=product1, order=order1, quantity=10, date_added=time)
        self.assertEqual(obj1.product, ProdukMasker.objects.get(nama='Masker kain'))
        self.assertEqual(obj1.order, Order.objects.get(user=User.objects.get(username='ogiorgil')))
        self.assertEqual(obj1.quantity, 10)
        self.assertEqual(obj1.get_total(), obj1.product.harga*obj1.quantity)

    # def test_cart_is_exist(self):
    #     response = self.client.get("/cart/")
    #     self.assertEqual(response.status_code, 200)

    # def test_cart(self):
    #     User.objects.create(username="ogiorgil", email="ogiorgil@localhost.com")
    #     self.client.login(username="ogiorgil", email="ogiorgil@localhost.com")
    #     user1 = User.objects.get(username="ogiorgil")
    #     order, created = Order.objects.get_or_create(user=user1, complete=False)
    #     items = order.orderitem_set.all()
    #     customs = order.custommask_set.all()
    #     response = self.client.get("/cart/")
    #     html_response = response.content.decode('utf8')
    #     self.assertEqual(response.status_code, 200)

    # def test_post_cart(self):
    #     response = self.client.post('/cart/')
    #     self.assertEqual(response.status_code, 200)

    # def test_valid_cart(self):
    #     dictio = {'note': 'masukin data'}
    #     response = self.client.post('/cart/', dictio)
    #     self.assertEqual(response.status_code, 200)

    # def test_order_data(self):
    #     user1 = User.objects.create(username="ogiorgil", email="ogiorgil@localhost.com")
    #     Order.objects.create(user=user1, complete=False, note='Sebuah Catatan')
    #     response = self.client.post('/cart/', {'user': user1, 'complete': False, 'note':'Sebuah Catatan'})
    #     self.assertEqual(response.status_code, 200)

    # def test_response_json(self):
    #     user = User.objects.create_user(
    #         first_name="user",
    #         last_name="name",
    #         email="user@email.com",
    #         username="username",
    #         password="user_password",
    #     )
    #     self.client.login(username="username", password="user_password")

    #     product = ProdukMasker.objects.create(
    #         id = '1',
    #         nama = 'Masker Kain',
    #         rating = 90,
    #         deskripsi = 'Deskripsi barang',
    #         harga = 11,
    #         stok = 100,
    #     )

    #     order, created = Order.objects.get_or_create(user=user, complete=False)
    #     orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    #     data = {
	# 		'productId' : 1,
    #         'action' : 'add',
    #         'quantity' : 0,
    #         'get-total' : 0,
    #         'get-items-total' : 0,
    #         'get-price-total' : 0,

	# 	}

    #     response = self.client.post('/update_item/')
    #     print(response.json())
    #     print(JsonResponse)
    #     self.assertEqual(True, isinstance(response, JsonResponse))