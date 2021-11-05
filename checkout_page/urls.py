from django.urls import path
from . import views

urlpatterns = [
    path('checkout-1', views.checkout_form),
    path('checkout-2', views.checkout2_form),
    path('checkout-3', views.checkout3_form),
    path('checkout-4', views.checkout4),
    path('calc', views.AjaxCalcPrice.as_view()),
    path('checkout-complete', views.checkout_complete)
]