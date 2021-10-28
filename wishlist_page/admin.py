from django.contrib import admin

# Register your models here.

from .models import WishlistItem

admin.site.register(WishlistItem)
