from django import forms
from checkout_page.models import Checkout, Pengiriman, Pembayaran

class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Checkout
        fields = ['name', 'email', 'telp', 'alamat']

class PengirimanForm(forms.ModelForm):
    class Meta:
        model = Pengiriman
        fields = ['durasi', 'kurir']

class PembayaranForm(forms.ModelForm):
    class Meta:
        model = Pembayaran
        fields = ['metode'] 