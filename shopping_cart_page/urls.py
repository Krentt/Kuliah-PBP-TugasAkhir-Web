from django.urls import path

from .views import *

app_name = "shopping_cart_page"

urlpatterns = [
    path("cart/", cart, name="cart"),
    path('update_item/', updateItem, name="update_item"),
]
