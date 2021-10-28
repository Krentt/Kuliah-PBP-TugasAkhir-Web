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
		customs = CustomMask.objects.all()
		cartItems = order.get_items_total
		form = NoteForm(request.POST or None)
		if request.method == 'POST':
			order.note = request.POST['note']
			order.save()
	else:
		items = []
		customs = []
		order = {'get_price_total':0, 'get_items_total':0}
		cartItems = order['get_items_total']
		form = NoteForm()

	context = {'items':items, 'order':order, 'cartItems':cartItems, 'form':form, 'customs':customs}
	return render(request, "shopping_cart_page.html", context)

def updateItem(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']
	
	customer = request.user.customer
	product = ProdukMasker.objects.get(id=productId)
	order, created = Order.objects.get_or_create(customer=customer, complete=False)

	orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

	if action == 'add':
		orderItem.quantity = orderItem.quantity + 1
	elif action == 'remove':
		orderItem.quantity = orderItem.quantity - 1
	elif action == 'removeAll':
		orderItem.quantity = 0

	orderItem.save()

	if orderItem.quantity == 0:
		orderItem.delete()

	return JsonResponse('item was added', safe=False)