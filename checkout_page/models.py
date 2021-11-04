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
        ('Next Day (1 hari) *Rp 10.000', 'Next Day (1 hari) *Rp 10.000'),
        ('Reguler (2-4 hari) *Rp 15.000', 'Reguler (2-4 hari) *Rp 15.000'),
    )
    KURIR = (
        ('AnterAja', 'AnterAja'),
        ('Tiki', 'Tiki'),
        ('JNE', "JNE"),
    )
    durasi = models.CharField(max_length=100, choices=DURASI)
    kurir = models.CharField(max_length=100, choices=KURIR)
    # if durasi == 'Next Day (1 hari)':
    #     harga = 10000
    # else:
    #     harga = 15000
    def cek_harga(self):
        if self.durasi == 'Next Day (1 hari) *Rp 10.000':
            return 10000
        else:
            return 15000

class Pembayaran(models.Model):
    # Referensi: Tokopedia
    METODE = (
        ('Mandiri Virtual Account', 'Mandiri Virtual Account'),
        ('BCA Virtual Account', 'BCA Virtual Account'),
        ('Bank BCA', 'Bank BCA'),
        ('Bank MANDIRI', 'Bank MANDIRI'),
    )
    metode = models.CharField(max_length=100, choices=METODE)

