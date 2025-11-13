# app_Petco/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio_petco, name='inicio_petco'),

    # URLs para Clientes
    path('clientes/', views.ver_clientes, name='ver_clientes'),
    path('clientes/agregar/', views.agregar_cliente, name='agregar_cliente'),
    path('clientes/actualizar/<int:pk>/', views.actualizar_cliente, name='actualizar_cliente'),
    path('clientes/borrar/<int:pk>/', views.borrar_cliente, name='borrar_cliente'),

    # URLs para Mascotas
    path('mascotas/', views.ver_mascotas, name='ver_mascotas'),
    path('mascotas/agregar/', views.agregar_mascota, name='agregar_mascota'),
    path('mascotas/actualizar/<int:pk>/', views.actualizar_mascota, name='actualizar_mascota'),
    path('mascotas/borrar/<int:pk>/', views.borrar_mascota, name='borrar_mascota'),

    # URLs para Productos
    path('productos/', views.ver_productos, name='ver_productos'),
    path('productos/agregar/', views.agregar_producto, name='agregar_producto'),
    path('productos/actualizar/<int:pk>/', views.actualizar_producto, name='actualizar_producto'),
    path('productos/borrar/<int:pk>/', views.borrar_producto, name='borrar_producto'),

    # URLs para Servicios
    path('servicios/', views.ver_servicios, name='ver_servicios'),
    path('servicios/agregar/', views.agregar_servicio, name='agregar_servicio'),
    path('servicios/actualizar/<int:pk>/', views.actualizar_servicio, name='actualizar_servicio'),
    path('servicios/borrar/<int:pk>/', views.borrar_servicio, name='borrar_servicio'),

    # URLs para Veterinarios
    path('veterinarios/', views.ver_veterinarios, name='ver_veterinarios'),
    path('veterinarios/agregar/', views.agregar_veterinario, name='agregar_veterinario'),
    path('veterinarios/actualizar/<int:pk>/', views.actualizar_veterinario, name='actualizar_veterinario'),
    path('veterinarios/borrar/<int:pk>/', views.borrar_veterinario, name='borrar_veterinario'),

    # URLs para Citas
    path('citas/', views.ver_citas, name='ver_citas'),
    path('citas/agregar/', views.agregar_cita, name='agregar_cita'),
    path('citas/actualizar/<int:pk>/', views.actualizar_cita, name='actualizar_cita'),
    path('citas/borrar/<int:pk>/', views.borrar_cita, name='borrar_cita'),
]