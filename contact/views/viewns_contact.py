from django.shortcuts import render
from contact.models import Contact
from django.http import Http404
from django.shortcuts import get_object_or_404


def index(request):
    contacts = Contact.objects.all().filter(show=True).order_by('-id')
    context = {
        'contacts': contacts,
    }
    return render(
        request,
        'contact/index.html',
        context,
    )


def single_contact(request, contact_id):
    single_contact = get_object_or_404(Contact, pk=contact_id, show=True)
    context = {
        'contact': single_contact,
    }

    return render(
        request,
        'contact/single_contact.html',
        context,
    )
