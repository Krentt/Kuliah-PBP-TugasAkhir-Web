from django.db import models

# Create your models here.
class UserForm(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    confirm_password = models.CharField(max_length=30)
