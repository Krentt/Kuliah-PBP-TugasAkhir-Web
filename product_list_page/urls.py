from django.urls import path
from .views import plp

app_name = "product_list_page"

urlpatterns = [
    path("product-list-page/", plp, name="plp"),
]