from django.urls import path
from .views import index, single_contact
from django.conf.urls.static import static
from django.conf import settings
app_name = 'contact'

urlpatterns = [
    path(
        '<int:contact_id>/',
        single_contact,
        name='contact'
    ),
    path(
        '',
        index,
        name='index'
    ),path(
        'search/',
        index,
        name='search'
    ),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
