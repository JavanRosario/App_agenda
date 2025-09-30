from django.contrib import admin
from .models import Contact, Category


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'id', 'first_name', 'phone', 'email', 'last_name','show'
    ordering = 'id',
    search_fields = 'id', 'first_name', 'id',
    list_per_page = 100
    list_max_show_all = 500
    list_editable = 'last_name', 'first_name', 'show',
    list_display_links = 'phone',


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'name',
    ordering = '-id',
