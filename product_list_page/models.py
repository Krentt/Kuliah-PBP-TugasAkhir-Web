from django.db import models

class ProdukMasker(models.Model):
    nama = models.CharField(max_length=255)
    rating = models.BigAutoField()
    deskripsi = models.CharField(max_length=255)
    harga = models.BigAutoField()
    stok = models.BigAutoField()