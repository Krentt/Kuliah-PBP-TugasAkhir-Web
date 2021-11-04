from django.test import TestCase
from .models import *
from django.test import Client

class ProductTest(TestCase):
    def test(self):
        response = Client().get("/product_list_page/")
        self.assertEqual(response.status_code, 200)

    def test_product(self):
        product = ProdukMasker.objects.create(
            id = '1',
            nama = 'Masker Kain',
            rating = 90,
            deskripsi = 'Deskripsi barang',
            harga = 11,
            stok = 100,
        )
        self.assertEqual(product.__str__(), product.nama)