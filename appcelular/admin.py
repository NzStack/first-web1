from django.contrib import admin
from .models import Celular, Cliente


class ClienteAdmin(admin.ModelAdmin):
    list_display = ['firstname', 'lastname', 'rut', 'email', 'phonenumber', 'address']

admin.site.register(Celular)
admin.site.register(Cliente, ClienteAdmin)