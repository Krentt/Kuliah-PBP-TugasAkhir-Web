from django.urls import path
from cuztomize_masker_page.views import custom_mask, update_deskripsi
from django.conf import settings
from django.conf.urls.static import static

app_name = "cuztomize_masker_page"
urlpatterns = [
    path('custom-mask/', custom_mask, name='custom_mask'),
    path('data-deskripsi/', update_deskripsi, name='update_deskripsi'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



