from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from checkout_page.models import Checkout, Pengiriman, Pembayaran
from checkout_page.forms import CheckoutForm, PengirimanForm, PembayaranForm
from shopping_cart_page.models import *

# Create your views here.
# Method Detail Pembayaran
def checkout_form(request):
    if request.method == 'POST': # Ngecek POST atau GET. POST itu protokol masukin data, GET itu buat ngambil data.
        form = CheckoutForm(request.POST)
        if form.is_valid():
            form.save()  # Simpan data di DB
            return HttpResponseRedirect('checkout-2')  # Redirect kalau sudah selesai

    else:
        # Delete semua object
        Checkout.objects.all().delete()
        form = CheckoutForm() # Buat form kosong

    return render(request, 'checkout_layout.html', {'form':form})

# Method Metode Pengiriman
def checkout2_form(request):
    if request.method == 'POST': # Ngecek POST atau GET. POST itu protokol masukin data, GET itu buat ngambil data.
        form = PengirimanForm(request.POST)
        if form.is_valid():
            form.save()  # Simpan data di DB
            return HttpResponseRedirect('checkout-3')  # Redirect kalau sudah selesai

    else:
        # Delete semua object
        Pengiriman.objects.all().delete()
        form = PengirimanForm() # Buat form kosong

    return render(request, 'checkout2_layout.html', {'form':form})

# Method Metode Pembayaran
def checkout3_form(request):
    if request.method == 'POST': # Ngecek POST atau GET. POST itu protokol masukin data, GET itu buat ngambil data.
        form = PembayaranForm(request.POST)
        if form.is_valid():
            form.save()  # Simpan data di DB
            return HttpResponseRedirect('checkout-4')  # Redirect kalau sudah selesai

    else:
        # Delete semua object
        Pembayaran.objects.all().delete()
        form = PembayaranForm() # Buat form kosong

    return render(request, 'checkout3_layout.html', {'form':form})

def checkout4(request):
    checkouts = Checkout.objects.all()  
    pengirimans = Pengiriman.objects.all()
    pembayarans = Pembayaran.objects.all()
    response = {'checkouts': checkouts,
                'pengirimans': pengirimans,
                'pembayarans': pembayarans}
    user = request.user
    order, created = Order.objects.get_or_create(user=user, complete=False)
    order.complete = True
    order.save()
    return render(request, 'checkout4_layout.html', response)


