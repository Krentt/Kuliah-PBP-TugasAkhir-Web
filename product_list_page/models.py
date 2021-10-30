from django.db import models

class ProdukMasker(models.Model):
    nama = models.CharField(max_length=255)
    rating = models.BigIntegerField()
    deskripsi = models.CharField(max_length=255)
    harga = models.BigIntegerField()
    stok = models.BigIntegerField()
    # image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.nama

    # @property
    # def imageURL(self):
    #     try:
    #         url = self.image.url
    #     except:
    #         url = ''
    #     return url