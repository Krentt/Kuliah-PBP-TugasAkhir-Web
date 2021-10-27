from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class WishlistItem(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    count = models.IntegerField()
