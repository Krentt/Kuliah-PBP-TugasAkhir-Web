from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import *
from product_list_page.models import *
from cuztomize_masker_page.models import *
from .forms import NoteForm

def cart(request):
	context = {}
	if request.user.is_authenticated:
		user = request.user
		order, created = Order.objects.get_or_create(user=user, complete=False)
		items = order.orderitem_set.all()
		customs = order.custommask_set.all()
		cartItems = order.get_items_total
		form = NoteForm(request.POST or None)
		if request.method == 'POST':
			order.note = request.POST['note']
			order.save()
	else:
		items = []
		customs = []
		order = {'get_price_total':0, 'get_items_total':0, 'get_total':0}
		cartItems = order['get_items_total']
		form = NoteForm()

	context = {'items':items, 'order':order, 'cartItems':cartItems, 'form':form, 'customs':customs}
	return render(request, "shopping_cart_page.html", context)

def updateItem(request):
	data = json.loads(request.body)
	productId = data['productId']
	
	user = request.user
	product = ProdukMasker.objects.get(id=productId)
	order, created = Order.objects.get_or_create(user=user, complete=False)

	orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
	orderItem.quantity = orderItem.quantity + 1

	orderItem.save()

	return JsonResponse(data)

def addItem(request):
	data = json.loads(request.body)
	productId = data['productId']
	
	user = request.user
	product = ProdukMasker.objects.get(id=productId)
	order, created = Order.objects.get_or_create(user=user, complete=False)

	orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
	orderItem.quantity = orderItem.quantity + 1
	orderItem.save()

	data["quantity"] = orderItem.quantity
	data["get-total"] = orderItem.get_total()
	data["get-items-total"] = order.get_items_total()
	data["get-price-total"] = order.get_price_total()

	return JsonResponse(data)


def subtractItem(request):
	data = json.loads(request.body)
	productId = data['productId']

	user = request.user
	product = ProdukMasker.objects.get(id=productId)
	order, created = Order.objects.get_or_create(user=user, complete=False)

	orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

	orderItem.quantity = orderItem.quantity - 1
	orderItem.save()
	
	data["quantity"] = orderItem.quantity
	data["get-total"] = orderItem.get_total()
	data["get-items-total"] = order.get_items_total()
	data["get-price-total"] = order.get_price_total()

	return JsonResponse(data)


def removeItem(request):
	data = json.loads(request.body)
	productId = data['productId']
	
	user = request.user
	product = ProdukMasker.objects.get(id=productId)
	order, created = Order.objects.get_or_create(user=user, complete=False)

	orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
	orderItem.quantity = 0
	orderItem.save()

	data["get-items-total"] = order.get_items_total()
	data["get-price-total"] = order.get_price_total()

	if orderItem.quantity == 0:
		orderItem.delete()

	return JsonResponse(data)