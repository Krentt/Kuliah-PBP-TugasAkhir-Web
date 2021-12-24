from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register_user),
    path('login', views.login_user, name="login"),
    path('home-page', views.home_page),
    path('logout', views.logout_user),
    path('login-flutter', views.login_flutter),
    path('register-flutter', views.register_flutter)
]