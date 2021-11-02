from django.urls import path
from .views import *

urlpatterns = [
    path("cart/", cart, name="cart"),
    path('update_item/', updateItem, name="update_item"),
    path('add_item/', addItem, name="add_item"),
    path('subtract_item/', subtractItem, name="subtract_item"),
    path('remove_item/', removeItem, name="remove_item"),
]
