from contact.forms import Form
from django.shortcuts import render


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
