from django.shortcuts import render
from django.views.generic import View
from django.http.response import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from checkout_page.models import Checkout, Pengiriman, Pembayaran
from checkout_page.forms import CheckoutForm, PengirimanForm, PembayaranForm
from shopping_cart_page.models import *
from django.http import JsonResponse

# User harus sudah login
@login_required(login_url='/login')
# Dilakukan objects.all().delete() pada setiap tahap agar hanya ada satu model dari masing-masing tahap 
# Method Detail Pembayaran
def checkout_form(request):
    if request.method == 'POST': 
        Checkout.objects.all().delete()
        form = CheckoutForm(request.POST)
        if form.is_valid():
            form.save()  # Simpan data di DB
            return HttpResponseRedirect('checkout-2')  # Redirect kalau sudah selesai

    else:
        # Jika cart kosong, return ke home
        user = request.user
        order, created = Order.objects.get_or_create(user=user, complete=False)
        if order.get_items_total() == 0:
            return HttpResponseRedirect('/')
        # Delete semua object
        Checkout.objects.all().delete()
        form = CheckoutForm() # Buat form kosong

    return render(request, 'checkout_layout.html', {'form':form})

@login_required(login_url='/login')
# Method Metode Pengiriman
def checkout2_form(request):
    if request.method == 'POST':
        Pengiriman.objects.all().delete()
        form = PengirimanForm(request.POST)
        if form.is_valid():
            form.save()  # Simpan data di DB
            return HttpResponseRedirect('checkout-3')  # Redirect kalau sudah selesai

    else:
        # Delete semua object
        Pengiriman.objects.all().delete()
        checkouts = Checkout.objects.all()
        # Redirect ke checkout-1 kalau user secara manual akses checkout-2
        if not checkouts.exists():
            return HttpResponseRedirect('checkout-1')
        form = PengirimanForm() # Buat form kosong
        response = {'checkouts':checkouts, 'form':form}

    return render(request, 'checkout2_layout.html', response)

@login_required(login_url='/login')
# Method Metode Pembayaran
def checkout3_form(request):
    if request.method == 'POST': 
        Pembayaran.objects.all().delete()
        form = PembayaranForm(request.POST)
        if form.is_valid():
            form.save()  # Simpan data di DB
            return HttpResponseRedirect('checkout-4')  # Redirect kalau sudah selesai

    else:
        # Delete semua object
        Pembayaran.objects.all().delete()
        checkouts = Checkout.objects.all()
        pengirimans = Pengiriman.objects.all()
        # Redirect ke checkout-1 kalau user secara manual akses checkout-3
        if not checkouts.exists() or not pengirimans.exists():
            return HttpResponseRedirect('checkout-1')
        form = PembayaranForm() # Buat form kosong
        response = {'checkouts':checkouts, 'pengirimans':pengirimans, 'form':form,}

    return render(request, 'checkout3_layout.html', response)

@login_required(login_url='/login')
# Method Konfirmasi Checkout
def checkout4(request):
    checkouts = Checkout.objects.all()  
    pengirimans = Pengiriman.objects.all()
    pembayarans = Pembayaran.objects.all()
    # Redirect ke checkout-1 kalau user secara manual akses checkout-4
    if not checkouts.exists() or not pengirimans.exists() or not pembayarans.exists():
        return HttpResponseRedirect('checkout-1')
    user = request.user
    order, created = Order.objects.get_or_create(user=user, complete=False)
    response = {'checkouts': checkouts,
                'pengirimans': pengirimans,
                'pembayarans': pembayarans,
                'user':user, 'order':order}

    return render(request, 'checkout4_layout.html', response)

@login_required(login_url='/login')
# Method Checkout Complete
def checkout_complete(request):
    checkouts = Checkout.objects.all()  
    pengirimans = Pengiriman.objects.all()
    pembayarans = Pembayaran.objects.all()
    # Redirect ke checkout-1 kalau user secara manual akses checkout-complete  
    if not checkouts.exists() and not pengirimans.exists() and not pembayarans.exists():
        return HttpResponseRedirect('checkout-1')
    Checkout.objects.all().delete()
    Pengiriman.objects.all().delete()
    Pembayaran.objects.all().delete()
    user = request.user
    order, created = Order.objects.get_or_create(user=user, complete=False)
    order.complete = True
    order.save()

    return render(request, 'checkout_complete.html')

@login_required(login_url='/login')
class AjaxCalcPrice(View):
    def get(self, request):
        if request.is_ajax():
            pengirimans = Pengiriman.objects.first()
            user = request.user
            order, created = Order.objects.get_or_create(user=user, complete=False)
            hargatotal = pengirimans.cek_harga() + order.get_price_total()
            return JsonResponse({'harga':hargatotal}, status=200)
            
        return render(request, 'checkout4_layout.html')

