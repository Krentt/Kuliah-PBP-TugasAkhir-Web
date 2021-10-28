from django.urls import path
from cuztomize_masker_page.views import custom_mask
from django.conf import settings
from django.conf.urls.static import static

app_name = "cuztomize_masker_page"
urlpatterns = [
    path('custom-mask/', custom_mask, name='custom_mask'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



