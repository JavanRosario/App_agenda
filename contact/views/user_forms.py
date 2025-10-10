from email import message
from django.shortcuts import render, redirect
from contact.forms import OwnerForm
from django.contrib import messages


def register(request):
    form = OwnerForm()

    if request.method == 'POST':
        form = OwnerForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Usuário criado com sucesso')
            return redirect('contact:index')

    return render(request, 'contact/register.html', {'form': form})
