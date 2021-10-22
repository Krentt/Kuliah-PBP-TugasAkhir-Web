from django.urls import path

from .views import scp

app_name = "shopping_cart_page"

urlpatterns = [
    path("shopping-cart-page/", scp, name="scp"),
]
