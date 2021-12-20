from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import *
from product_list_page.models import *
from cuztomize_masker_page.models import *
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from .forms import NoteForm
from django.forms.models import model_to_dict

def cart(request):
	context = {}
	if request.user.is_authenticated:
		order, created = Order.objects.get_or_create(user=request.user, complete=False)
		items = order.orderitem_set.all()
		customs = order.custommask_set.all()
		form = NoteForm(request.POST or None)
		items = order.orderitem_set.all()
		if request.method == 'POST':
			order.note = request.POST['note']
			order.save()
	else:
		items = customs = order = []
		form = NoteForm()
		
	context = {'items':items, 'order':order, 'form':form, 'customs':customs}
	return render(request, "shopping_cart_page.html", context)

def updateItem(request):
	if len(request.body) == 0:
		data = {'productId':'1', 'action': 'remove'}
	else:
		data = json.loads(request.body)

	product = ProdukMasker.objects.get(id=data['productId'])
	order, created = Order.objects.get_or_create(user=request.user, complete=False)
	orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

	if (data['action'] == 'add'):
		orderItem.quantity = orderItem.quantity + 1
	elif (data['action'] == 'subtract'):
		orderItem.quantity = orderItem.quantity - 1
	elif (data['action'] == 'remove'):
		orderItem.quantity = 0

	orderItem.save()

	if orderItem.quantity == 0:
		orderItem.delete()

	data["quantity"] = orderItem.quantity
	data["get-total"] = orderItem.get_total()
	data["get-items-total"] = order.get_items_total()
	data["get-price-total"] = order.get_price_total()
	
	return JsonResponse(data)

@csrf_exempt
def orderJson(request):
    if request.method == 'POST':
        print(request.body)
        data = json.loads(request.body)
        print(data)
        # user = data["user"]
        # note = data["note"]
        # order, created = Order.objects.get_or_create(user=user, complete=False)
        # order.note = note
    
    if request.user.is_authenticated:
        order, created = Order.objects.get_or_create(user=request.user, complete=False)
        dataorder = model_to_dict(order)

    else:
        dataorder = {}
        # dataorder = {'id': 3, 'user': 3, 'complete': False, 'note': 'Ini sebuah catatan'}
    
    # print(dataorder)
    return JsonResponse(dataorder, safe=False)

@csrf_exempt
def itemJson(request):
    if request.method == 'POST':
        print(request.body)
        data = json.loads(request.body)
        print(data)
        # order = data["order"]
        # product = data["product"]
        # quantity = data["quantity"]
        # orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
        # if quantity = 0:
        #     orderItem.delete()
        # else:
        #     orderItem.quantity = quantity
        #     orderItem.save()
    
    if request.user.is_authenticated:
        order, created = Order.objects.get_or_create(user=request.user, complete=False)
        items = order.orderitem_set.all()
        dataitems = serializers.serialize('json', items)
        dataitems = json.loads(dataitems)
    else:
        items = []
        dataitems = serializers.serialize('json', items)
        # dataitems = '[{"model": "shopping_cart_page.orderitem", "pk": 4, "fields": {"product": 2, "order": 3, "quantity": 2, "date_added": "2021-12-17T11:59:03.541Z"}}, {"model": "shopping_cart_page.orderitem", "pk": 5, "fields": {"product": 1, "order": 3, "quantity": 1, "date_added": "2021-12-19T02:54:56.496Z"}}]'
        dataitems = json.loads(dataitems)
    # print(dataitems)
    return JsonResponse(dataitems, safe=False)

def productJson(request):
    if request.user.is_authenticated:
        order, created = Order.objects.get_or_create(user=request.user, complete=False)
        items = order.orderitem_set.all()
        dataproducts = []
        for i in items:
            dataproducts.append(i.product)
        dataproducts = serializers.serialize('json', dataproducts)
        dataproducts = json.loads(dataproducts)
    else:
        dataproducts = []
        dataproducts = serializers.serialize('json', dataproducts)
        # dataproducts = '[{"model": "product_list_page.produkmasker", "pk": 2, "fields": {"nama": "Plague Mask", "rating": 11, "deskripsi": "Deskripsi Plague Mask", "harga": 11, "stok": 24, "image": "image/upload/v1638871626/ProdukMasker/unrdc9dgeoyr5pyqmfxh.png"}}, {"model": "product_list_page.produkmasker", "pk": 1, "fields": {"nama": "Chemical Mask", "rating": 11, "deskripsi": "Deskripsi Chemical Mask", "harga": 11, "stok": 24, "image": "image/upload/v1638864884/ProdukMasker/djni0tval1kvkj1retr6.png"}}]'
        dataproducts = json.loads(dataproducts)
    # print(dataproducts)
    return JsonResponse(dataproducts, safe=False)

def customJson(request):
    if request.user.is_authenticated:
        order, created = Order.objects.get_or_create(user=request.user, complete=False)
        customs = order.custommask_set.all()
        datacustoms = serializers.serialize('json', customs)
        datacustoms = json.loads(datacustoms)
    else:
        customs = []
        datacustoms = serializers.serialize('json', customs)
        # datacustoms = '[{"model": "cuztomize_masker_page.custommask", "pk": 2, "fields": {"sex": "F", "size": "XL", "model": "SURGICAL", "color": "RED", "style": "image/upload/v1639746424/custom-mask-style/fftiwdkbkxkdb1p9utzy.png", "price": 15.0, "quantity": 100, "order": 3}}, {"model": "cuztomize_masker_page.custommask", "pk": 3, "fields": {"sex": "M", "size": "L", "model": "SPONGE", "color": "RED", "style": "image/upload/v1639882890/custom-mask-style/ea2sv3jejc7nw9vmyecl.png", "price": 15.0, "quantity": 100, "order": 3}}]'
        datacustoms = json.loads(datacustoms)
    # print(datacustoms)
    return JsonResponse(datacustoms, safe=False)

def getJson(request):
    jsonget = {}
    
    if request.user.is_authenticated:
        order, created = Order.objects.get_or_create(user=request.user, complete=False)
        jsonget["get_price_total"] = order.get_price_total()
        jsonget["get_items_total"] = order.get_items_total()
    else:
        jsonget["get_price_total"] = 0  
        jsonget["get_items_total"] = 0
    
    return JsonResponse(jsonget, safe=False)