from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from .forms import ProdukMaskerForm
from .models import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import JsonResponse
import json
from product_list_page.models import *
from cuztomize_masker_page.models import *
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def plp(request):
    product = ProdukMasker.objects.all()
    response = {'product': product}
    return render(request, 'product_list_page.html', response)

@login_required(login_url="../login")
def add_mask(request):
    if request.method == 'POST':
        form = ProdukMaskerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/product_list_page/')
    else:
        form = ProdukMaskerForm()
    return render(request, 'product_form.html', {'form': form})

@csrf_exempt
def addJson(request):
    data = {}
    if request.user.is_authenticated:
        if request.method == 'POST':
            data = json.loads(request.body)
            product = ProdukMasker.objects.get(id=int(data['productId']))
            order, created = Order.objects.get_or_create(user=request.user, complete=False)
            orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
            orderItem.quantity = orderItem.quantity + 1
            orderItem.save()
    return JsonResponse(data)