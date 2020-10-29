from django.shortcuts import render
from .models import Celular


def index(request):
    return render(request, 'appcelular/index.html', {})

def celulares1(request):
    return render(request, 'appcelular/celulares1.html', {})

def mail(request):
    return render(request, 'appcelular/mail.html', {})