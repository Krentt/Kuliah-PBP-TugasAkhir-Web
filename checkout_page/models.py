from django.db import models

# Create your models here.

class Checkout(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField()
    telp = models.IntegerField()
    alamat = models.TextField()

class Pengiriman(models.Model):
    # Referensi: Tokopedia
    DURASI = (
        (15000, 'Next Day (1 hari)'),
        (10000, 'Reguler (2-4 hari)'),
    )
    KURIR = (
        (13000, 'AnterAja'),
        (15000, 'Tiki'),
        (14000, "JNE"),
    )
    durasi = models.CharField(max_length=2, choices=DURASI)
    kurir = models.CharField(max_length=2, choices=KURIR)

class Pembayaran(models.Model):
    # Referensi: Tokopedia
    METODE = (
        ('Mandiri', 'Mandiri Virtual Account'),
        ('BCA', 'BCA Virtual Account'),
        ('BankBCA', 'Bank BCA'),
        ('BankMANDIRI', 'Bank MANDIRI'),
    )
    metode = models.CharField(max_length=11, choices=METODE)

