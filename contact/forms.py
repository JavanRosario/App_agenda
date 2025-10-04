from django import forms
from django.core.exceptions import ValidationError
from .models import Contact
from typing import Any

class Form(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'phone',)

    def clean(self) -> dict[str, Any]:
        cleaned_data = self.cleaned_data
        self.add_error('first_name', ValidationError(
            'Erro no nome', code='invalid'))
        return super().clean()


