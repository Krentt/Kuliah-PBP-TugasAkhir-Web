from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from checkout_page.models import Checkout, Pengiriman, Pembayaran
from checkout_page.forms import CheckoutForm, PengirimanForm, PembayaranForm

# Create your views here.
# Method Detail Pembayaran
def checkout_form(request):
    if request.method == 'POST': # Ngecek POST atau GET. POST itu protokol masukin data, GET itu buat ngambil data.
        form = CheckoutForm(request.POST)
        if form.is_valid():
            form.save()  # Simpan data di DB
            return HttpResponseRedirect('checkout-2')  # Redirect kalau sudah selesai

    else:
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
        Pembayaran.objects.all().delete()
        form = PembayaranForm() # Buat form kosong

    return render(request, 'checkout3_layout.html', {'form':form})

def checkout4(request):
    checkout = Checkout.objects.all()  
    pengiriman = Pengiriman.objects.all()
    pembayaran = Pembayaran.objects.all()
    response = {'checkout': checkout,
                'pengiriman': pengiriman,
                'pembayaran': pembayaran}
    return render(request, 'checkout4.html', response)


