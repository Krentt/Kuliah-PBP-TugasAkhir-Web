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
		order, created = Order.objects.get_or_create(user=request.user, complete=False)
		items = order.orderitem_set.all()
		customs = order.custommask_set.all()
		form = NoteForm(request.POST or None)
		if request.method == 'POST':
			order.note = request.POST['note']
			order.save()
	else:
		items = customs = order = []
		form = NoteForm()
	context = {'items':items, 'order':order, 'form':form, 'customs':customs}
	return render(request, "shopping_cart_page.html", context)

def updateItem(request):
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