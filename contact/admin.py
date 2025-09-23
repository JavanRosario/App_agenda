from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'id','first_name', 'phone','email','last_name',
    ordering = 'id',
    # list_filter = 'created_date',
    search_fields = 'id','first_name','id',
    list_per_page = 1
    list_max_show_all =500
    list_editable = 'last_name','first_name',
    list_display_links ='phone',