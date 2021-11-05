from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('ajax/get_image', get_image),
    path('ajax/subscribe', subscribe),
    path('all_email', get_all_mail),
    path('unsubscribe/<id>', unsubscribe),
]