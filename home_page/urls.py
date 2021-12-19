from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('ajax/get_image', get_image),
    path('ajax/subscribe', subscribe),
    path('unsubscribe/<id>', unsubscribe),
    path('api/mobile/get-data/<max_data>', mobile_get_data),
    path('api/mobile/subscribe', mobile_subscribe),
]