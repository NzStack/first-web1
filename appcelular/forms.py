from django import forms
from django.forms import ModelForm
from .models import Cliente


class ClienteForm(ModelForm):

    firstname = forms.CharField(min_length=2, max_length=40)
    lastname = forms.CharField(min_length=2, max_length=20)
    rut = forms.CharField(max_length=15)
    email = forms.CharField(min_length=5, max_length=50)
    phonenumber = forms.CharField(min_length=11, max_length=12)
    address = forms.CharField(max_length=50)
    
    class Meta:
        model = Cliente
        fields = ['firstname', 'lastname', 'rut', 'email', 'phonenumber', 'address']
