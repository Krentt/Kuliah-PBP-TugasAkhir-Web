from django.db import models

# Create your models here.


class WishlistItem(models.Model):
    name = models.CharField(max_length=30)
    count = models.IntegerField()

class SubscribedEmail(models.Model):
    email = models.EmailField(unique=True)
