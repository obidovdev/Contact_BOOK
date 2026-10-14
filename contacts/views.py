from django.shortcuts import render, redirect, get_object_or_404
from .models import ContactBook
from .forms import ContactBookForm
def contact_list(request):
    contacts = ContactBook.objects.all().order_by('-created_at')
    return render(request, 'contacts/contact_list.html', {
        'contacts': contacts
    })

def contact_create(request):
    if request.method == 'POST':
        form = ContactBookForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('contact_list')
    else:
        form = ContactBookForm()

    return render(request, 'contacts/contact_form.html', {
        'form': form,
        'title': 'Yangi kontakt'
    })
def contact_update(request, pk):
    contact = get_object_or_404(ContactBook, pk=pk)

    if request.method == 'POST':
        form = ContactBookForm(request.POST, instance=contact)

        if form.is_valid():
            form.save()
            return redirect('contact_list')
    else:
        form = ContactBookForm(instance=contact)

    return render(request, 'contacts/contact_form.html', {
        'form': form,
        'title': 'Kontaktni tahrirlash'
    })
def contact_delete(request, pk):
    contact = get_object_or_404(ContactBook, pk=pk)

    if request.method == 'POST':
        contact.delete()
        return redirect('contact_list')

    return render(request, 'contacts/contact_confirm_delete.html', {
        'contact': contact
    })
