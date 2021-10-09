from django import path

from . import views

app_name = "home"

urlpatterns = [
    path("", views.index, name="index"),
]
