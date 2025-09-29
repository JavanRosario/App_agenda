from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Category(models.Model):
    class Meta:
        verbose_name = 'Category'

    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name


class Contact(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45, blank=True)
    phone = models.CharField(max_length=45)
    email = models.EmailField(max_length=254)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    show = models.BooleanField(default=True)
    image = models.ImageField(blank=True, upload_to='img/%Y/%m')
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
