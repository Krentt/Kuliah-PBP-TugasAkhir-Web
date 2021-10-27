from django.shortcuts import render

from django.views.generic import View, ListView
from .models import WishlistItem
from django.http import JsonResponse

# Create your views here.


def index(request):
    if request.user.is_authenticated:
        wishlists = WishlistItem.objects.filter(owner=request.user)
        response = {"wishlists": wishlists}
        return render(request, "wishlist_page/wishlist_index.html", response)
    else:
        return render(request, "wishlist_page/wishlist_index.html")


class CrudView(ListView):
    model = WishlistItem
    template_name = "wishlist_page/wishlist_index.html"
    context_object_name = "wishlists"


class CreateWishlistItem(View):
    def get(self, request):
        name1 = request.GET.get("name", None)
        price1 = request.GET.get("price", None)
        count1 = request.GET.get("count", None)

        obj = WishlistItem.objects.create(
            owner=request.user, name=name1, price=price1, count=count1
        )

        item = {
            "id": obj.id,
            "name": obj.name,
            "price": obj.price,
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
        obj.name = name1
        obj.price = price1
        obj.count = count1
        obj.save()

        item = {
            "id": obj.id,
            "name": obj.name,
            "price": "Rp" + obj.price,
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
