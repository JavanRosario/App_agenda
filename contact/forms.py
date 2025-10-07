# type: ignore
from cProfile import label
from django import forms
from django.core.exceptions import ValidationError
from .models import Contact


class Form(forms.ModelForm):
    image = forms.ImageField(
        widget=forms.FileInput(attrs={'accept': 'image/*'},), required=False, label='Imagem')


    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'phone',
                  'email', 'description', 'category', 'image')

    def clean(self):
        error_msg = ValidationError(
            'Primeiro nome não pode ser igual ao sobrenome', code='invalid')
        cleaned_data = self.cleaned_data
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')

        if first_name == last_name:
            self.add_error('first_name', error_msg)
            self.add_error('last_name', error_msg)
        return super().clean()

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')

        return first_name
