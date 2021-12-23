from django.urls import path
from .views import *

urlpatterns = [
    path("cart/", cart, name="cart"),
    path('update_item/', updateItem, name="update_item"),
    path('order_json/', orderJson, name="order_json"),
    path('item_json/', itemJson, name="item_json"),
    path('product_json/', productJson, name="product_json"),
    path('custom_json/', customJson, name="custom_json"),
    path('get_json/', getJson, name="get_json"),
]