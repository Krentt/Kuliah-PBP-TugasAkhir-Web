from django.urls import path
from . import views

urlpatterns = [
    path("wishlist/", views.index),
    path("request-data/", views.request_data),
    path("request-all-data/", views.request_all_data),
    path("post-data/", views.post_data),
    path("flutter-login/", views.flutter_login),
    path("ajax/create/", views.CreateWishlistItem.as_view(), name="create_item"),
    path("ajax/update/", views.UpdateWishlistItem.as_view(), name="update_item"),
    path("ajax/delete/", views.DeleteWishlistItem.as_view(), name="delete_item"),
]
