from django.db import models
from shopping_cart_page.models import *

# Create your models here.
class CustomMask (models.Model):
    SEX_CHOICES = (
        ('F', 'Female'),
        ('M', 'Male'),
        ('U', 'Unisex'),
    )

    SIZE_CHOICES = (
        ('XL', 'Extra Large'),
        ('L', 'Large'),
        ('M', 'Medium'),
        ('S', 'Small'),
    )

    MODEL_CHOICES = (
        ('SURGICAL','Surgical'),
        ('SPONGE','Sponge'),
        ('PITTA','Pitta'),
        ('CLOTH','Cloth'),
    )
    
    COLOR_CHOICES = (
        ('RED','Red'),
        ('GREEN','Green'),
        ('BLUE','Blue'),
        ('BLACK','Black'),
    )

    # product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    sex = models.CharField(max_length=8, choices=SEX_CHOICES, default=None, blank=False)
    size = models.CharField(max_length=8, choices=SIZE_CHOICES, default=None, blank= False)
    model = models.CharField(max_length=8, choices=MODEL_CHOICES, default=None, blank=False)
    color = models.CharField(max_length=8, choices=COLOR_CHOICES, default=None, blank=False)
    style = models.FileField(upload_to='custom-mask-style/', default=None)
    price = models.FloatField(default=15)
    quantity = models.IntegerField(default = 100, null = True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    
    def get_total(self):
        total = self.price * self.quantity
        return total

