from django.urls import path
from .views import index, mail, celulares1, listado_cliente, nuevo_cliente, modificar_cliente, eliminar_cliente


urlpatterns = [
    path('', index, name="index"),
    path('mail/', mail, name="mail"),
    path('celulares/', celulares1, name="celulares1"),
    path('listado-clientes', listado_cliente, name="listado_clientes"),
    path('nuevo-cliente', nuevo_cliente, name="nuevo_cliente"),
    path('modificar-cliente/<id>/', modificar_cliente, name="modificar_cliente"),
    path('eliminar-cliente/<id>/', eliminar_cliente, name="eliminar_cliente"),
]
    