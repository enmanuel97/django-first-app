from . import views
from django.urls import path

urlpatterns = [    
    path('', views.redirecttoClientes),
    path('clientes', views.listarClientes, name='clientes'),
    path('clientes/crear', views.crearCliente, name='crear-cliente'),
    path('clientes/detalles/<int:id>', views.verCliente, name='ver-cliente'),
    path('clientes/editar/<int:id>', views.actualizarCliente, name='actualizar-cliente'),
    path('clientes/eliminar/<int:id>', views.eliminarCliente, name='eliminar-cliente'),
]