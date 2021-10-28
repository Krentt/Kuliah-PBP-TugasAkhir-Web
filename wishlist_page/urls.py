from django.urls import path
from . import views

urlpatterns = [
    path("wishlist/", views.index),
    path("ajax/create/", views.CreateWishlistItem.as_view(), name="create_item"),
    path("ajax/update/", views.UpdateWishlistItem.as_view(), name="update_item"),
    path("ajax/delete/", views.DeleteWishlistItem.as_view(), name="delete_item"),
]
