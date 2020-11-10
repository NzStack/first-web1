from django.shortcuts import render, redirect
from .models import Celular, Cliente
from .forms import ClienteForm
from django.contrib.auth.decorators import login_required, permission_required



def index(request):
    return render(request, 'appcelular/index.html', {})

def celulares1(request):
    return render(request, 'appcelular/celulares1.html', {})

def mail(request):
    return render(request, 'appcelular/mail.html', {})

@permission_required('appcelular.add_cliente')
def listado_cliente(request):
    clientes = Cliente.objects.all()
    data = {
        'clientes':clientes
    }
    return render(request, 'appcelular/listado_clientes.html', data)



def nuevo_cliente(request):
    data = {
        'form':ClienteForm()
    }

    if request.method == 'POST':
        formulario = ClienteForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Guardado Correctamente"
            
    return render(request, 'appcelular/nuevo_cliente.html', data)

@login_required
def modificar_cliente(request, id):
    cliente = Cliente.objects.get(id=id)
    data = {
        'form': ClienteForm(instance=cliente)
    }

    if request.method == 'POST':
        formulario = ClienteForm(data=request.POST, instance=cliente)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Modificado Correctamente"
            data['form'] = formulario

    return render(request, 'appcelular/modificar_cliente.html', data)


@login_required
def eliminar_cliente(request, id):
    cliente = Cliente.objects.get(id=id)
    cliente.delete()

    return redirect(to="listado_clientes")

