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
        ('Next Day', 'Next Day (1 hari)'),
        ('Reguler', 'Reguler (2-4 hari)'),
    )
    KURIR = (
        ('AnterAja', 'AnterAja'),
        ('Tiki', 'Tiki'),
        ('JNE', "JNE"),
    )
    durasi = models.CharField(max_length=100, choices=DURASI)
    kurir = models.CharField(max_length=100, choices=KURIR)

class Pembayaran(models.Model):
    # Referensi: Tokopedia
    METODE = (
        ('Mandiri', 'Mandiri Virtual Account'),
        ('BCA', 'BCA Virtual Account'),
        ('BankBCA', 'Bank BCA'),
        ('BankMANDIRI', 'Bank MANDIRI'),
    )
    metode = models.CharField(max_length=100, choices=METODE)

