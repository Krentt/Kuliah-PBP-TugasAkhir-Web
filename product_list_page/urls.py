from django.urls import path
from .views import *

app_name = "product_list_page"

urlpatterns = [
    path("product_list_page/", plp, name="product_list_page"),
    path("product_form/", add_mask, name="product_form"),
    path('add_json/', addJson, name="add_json"),
]