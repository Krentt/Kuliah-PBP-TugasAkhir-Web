from django.shortcuts import render

from django.views.generic import View
from .models import WishlistItem
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import json
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User

# Create your views here.


@csrf_exempt
def request_all_data(request):
    # objs = WishlistItem.objects.get(owner=1)
    objs = WishlistItem.objects.all()
    data = serializers.serialize("json", objs)
    struct = json.loads(data)
    # data = json.dumps(struct[0])
    print(data)

    # returns list of maps
    return JsonResponse(struct, safe=False)


@csrf_exempt
def request_data(request):
    if request.method == "GET":
        # data = json.loads(request.body)
        owner_id = request.GET.get("owner_id")
        print(owner_id)
        # if request.user.is_authenticated:
        objs = WishlistItem.objects.filter(owner=owner_id)
        data = serializers.serialize("json", objs)
        struct = json.loads(data)
        # data = json.dumps(struct[0])
        print(data)
        # returns list of maps
        return JsonResponse(struct, safe=False)
        # else:
        #     return JsonResponse({"status": False}, safe=False)

    else:
        return JsonResponse({"status": False}, safe=False)


@csrf_exempt
def post_data(request):
    data = json.loads(request.body)
    print(request)
    user = int(data["user"])
    name = data["name"]
    price = int(data["price"])
    count = int(data["count"])
    User
    item, created = WishlistItem.objects.get_or_create(
        owner_id=user, name=name, price=price, count=count
    )
    return JsonResponse({"status": True}, safe=False)


@csrf_exempt
def flutter_login(request):
    if request.method == "POST":
        data = json.loads(request.body)
        print(data)
        username = data["username"]
        password = data["password"]

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse(
                {
                    "status": True,
                    "username": username,
                    "user_id": user.id,
                    "user": user,
                }
            )
        else:
            return JsonResponse({"status": False})


def index(request):
    if request.user.is_authenticated:
        wishlists = WishlistItem.objects.filter(owner=request.user)
        response = {"wishlists": wishlists}
        return render(request, "wishlist_page/wishlist_index.html", response)
    else:
        return render(request, "wishlist_page/wishlist_index.html")


class CreateWishlistItem(View):
    def get(self, request):
        name1 = request.GET.get("name", None)
        price1 = request.GET.get("price", None)
        count1 = request.GET.get("count", None)

        obj = WishlistItem.objects.create(
            owner=request.user, name=name1, price=price1, count=count1
        )
        obj_counts = WishlistItem.objects.count()

        add_zeros = ""
        if len(price1) < 3 or price1[-3] != ".":
            add_zeros = ".00"

        item = {
            "id": obj.id,
            "counter": obj_counts,
            "name": obj.name,
            "price": obj.price + add_zeros,
            "count": obj.count,
        }
        data = {"item": item}

        return JsonResponse(data)


class UpdateWishlistItem(View):
    def get(self, request):
        id1 = request.GET.get("id", None)
        name1 = request.GET.get("name", None)
        price1 = request.GET.get("price", None)
        count1 = request.GET.get("count", None)

        obj = WishlistItem.objects.get(id=id1)
        obj_counts = WishlistItem.objects.count()
        obj.name = name1
        obj.price = price1
        obj.count = count1
        obj.save()

        add_zeros = ""
        if len(price1) < 3 or price1[-3] != ".":
            add_zeros = ".00"

        print(price1, len(price1))

        item = {
            "id": obj.id,
            "counter": obj_counts,
            "name": obj.name,
            "price": "$" + obj.price + add_zeros,
            "count": obj.count,
        }
        data = {"item": item}

        return JsonResponse(data)


class DeleteWishlistItem(View):
    def get(self, request):
        id1 = request.GET.get("id", None)
        WishlistItem.objects.get(id=id1).delete()
        data = {"deleted": True}
        return JsonResponse(data)
