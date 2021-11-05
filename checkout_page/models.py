from django.db import models

# Create your models here.

class Checkout(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField()
    telp = models.BigIntegerField()
    alamat = models.TextField()

class Pengiriman(models.Model):
    # Referensi: Tokopedia
    DURASI = (
        ('Next Day (1 hari)', 'Next Day (1 hari) *$3'),
        ('Reguler (2-4 hari)', 'Reguler (2-4 hari) *$1'),
    )
    KURIR = (
        ('AnterAja', 'AnterAja'),
        ('Tiki', 'Tiki'),
        ('JNE', "JNE"),
    )
    durasi = models.CharField(max_length=100, choices=DURASI)
    kurir = models.CharField(max_length=100, choices=KURIR)

    def cek_harga(self):
        if self.durasi == 'Next Day (1 hari)':
            return 3
        else:
            return 1

class Pembayaran(models.Model):
    # Referensi: Tokopedia
    METODE = (
        ('Mandiri Virtual Account', 'Mandiri Virtual Account'),
        ('BCA Virtual Account', 'BCA Virtual Account'),
        ('Bank BCA', 'Bank BCA'),
        ('Bank MANDIRI', 'Bank MANDIRI'),
    )
    metode = models.CharField(max_length=100, choices=METODE)

