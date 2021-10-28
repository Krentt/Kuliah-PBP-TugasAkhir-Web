from django.db import models

class ProdukMasker(models.Model):
    nama = models.CharField(max_length=255)
    rating = models.BigIntegerField()
    deskripsi = models.CharField(max_length=255)
    harga = models.BigIntegerField()
    stok = models.BigIntegerField()