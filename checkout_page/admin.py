from django.contrib import admin
from checkout_page.models import Checkout, Pengiriman, Pembayaran

# Register your models here.
admin.site.register(Checkout)
admin.site.register(Pengiriman)
admin.site.register(Pembayaran)
