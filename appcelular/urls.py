from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index.html'),
    path('mail.html', views.mail, name='mail.html'),
    path('celulares1.html', views.celulares1, name='celulares1.html'),
]
    