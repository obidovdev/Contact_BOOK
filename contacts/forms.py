
from django import forms
from .models import ContactBook


class ContactBookForm(forms.ModelForm):
    class Meta:
        model = ContactBook
        fields = ['name', 'phone']
