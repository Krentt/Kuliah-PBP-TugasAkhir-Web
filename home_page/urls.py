from django.urls import path
from .views import index, get_image, subscribe, get_all_mail

urlpatterns = [
    path('', index),
    path('ajax/get_image', get_image),
    path('ajax/subscribe', subscribe),
    path('all_email', get_all_mail)
]