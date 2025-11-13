from django.contrib import admin
from .models import Cliente, Mascota, Producto, Servicio, Veterinario, Cita

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Mascota)
admin.site.register(Producto)
admin.site.register(Servicio)
admin.site.register(Veterinario)
admin.site.register(Cita)