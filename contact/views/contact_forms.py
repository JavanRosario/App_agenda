# type: ignore
from typing import Any
from django.shortcuts import render
from contact.models import Contact
from django.shortcuts import get_object_or_404, redirect
from django.db.models import Q
from django.core.paginator import Paginator
from django import forms
from django.core.exceptions import ValidationError


class Form(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'phone',)

    def clean(self) -> dict[str, Any]:
        cleaned_data = self.cleaned_data
        self.add_error('first_name',ValidationError('Erro no nome',code='invalid'))
        return super().clean()



def create(request):

    if request.method == 'POST':
        context = {
            'form': Form(request.POST)

        }
        return render(
            request,
            'contact/create.html',
            context,
        )
    context = {
            'form': Form()

        }
    return render(
            request,
            'contact/create.html',
            context,
        )
