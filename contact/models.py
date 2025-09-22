from django.db import models
from django.utils import timezone


class Contact(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45, blank=True)
    phone = models.CharField(max_length=45)
    email = models.EmailField(max_length=254)
    crated_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
