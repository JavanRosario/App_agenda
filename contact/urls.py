from django.urls import path
from .views import index, single_contact, search, create, update, delete,register
from django.conf.urls.static import static
from django.conf import settings
app_name = 'contact'

urlpatterns = [
    path('', index, name='index'),
    path('search/', search, name='search'),
    path('contact/<int:contact_id>/detail/', single_contact, name='contact'),
    path('contact/create/', create, name='create'),
    path('contact/<int:contact_id>/update/', update, name='update'),
    path('contact/<int:contact_id>/delete/', delete, name='delete'),
    path('user/create', register, name='register')

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
