from django.shortcuts import render
from contact.forms import OwnerForm


def register(request):
    form = OwnerForm()

    if request.method == 'POST':
        form = OwnerForm(request.POST)

        if form.is_valid():
            form.save()
            
    return render(request, 'contact/register.html', {'form': form})
