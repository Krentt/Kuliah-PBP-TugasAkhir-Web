"""TugasKelompok URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("testing/", include("home.urls")),
    path("", include("login_page.urls")),
    path("", include("home_page.urls")),
    path("", include("shopping_cart_page.urls")),
    path("", include("product_list_page.urls")),
    path("", include("wishlist_page.urls")),
    path("", include("checkout_page.urls")),
    path("", include("cuztomize_masker_page.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
