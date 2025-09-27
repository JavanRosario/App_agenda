from django.urls import path
from .views import index
from django.conf.urls.static import static
from django.conf import settings
app_name = 'contact'

urlpatterns = [
    path(
        '',
        index,
        name='index'
    )
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_ROOT, document_root=settings.STATIC_ROOT)
