# type: ignore
from django.shortcuts import render
from contact.models import Contact
from django.shortcuts import get_object_or_404, redirect
from django.db.models import Q


def index(request):
    contacts = Contact.objects.all().filter(show=True).order_by('-id')
    context = {
        'contacts': contacts,
        'main_title': 'Contatos - ',
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
        'single_title': f'{single_contact.first_name} {single_contact.last_name} - '
    }

    return render(
        request,
        'contact/single_contact.html',
        context,
    )


def search(request):
    search_value = request.GET.get('q', '').strip()

    if search_value == '':
        return redirect('contact:index')
    contacts = Contact.objects.all().filter(show=True).filter(Q(first_name__icontains=search_value) | Q(last_name__icontains=search_value)
                                                              | Q(phone_name__icontains=search_value) | Q(email_name__icontains=search_value)).order_by('-id')
    context = {
        'contacts': contacts,
        'main_title': 'Contatos - ',
    }
    return render(
        request,
        'contact/index.html',
        context,
    )
