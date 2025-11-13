from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente, Mascota, Producto, Servicio, Veterinario, Cita
from django.db.models import F # Para usar F-expressions si fuera necesario en el futuro
from datetime import datetime

# Create your views here.
def inicio_petco(request):
    return render(request, 'inicio.html')

# ==========================================
# FUNCIONES CRUD PARA CLIENTES
# ==========================================

def ver_clientes(request):
    clientes = Cliente.objects.all().order_by('apellido', 'nombre')
    context = {'clientes': clientes}
    return render(request, 'cliente/ver_clientes.html', context)

def agregar_cliente(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        email = request.POST.get('email')
        telefono = request.POST.get('telefono')
        direccion = request.POST.get('direccion')

        if nombre and apellido and email:
            Cliente.objects.create(nombre=nombre, apellido=apellido, email=email, telefono=telefono, direccion=direccion)
            return redirect('ver_clientes')
        else:
            context = {'error': 'Por favor, completa todos los campos obligatorios.'}
            return render(request, 'cliente/agregar_cliente.html', context)
    return render(request, 'cliente/agregar_cliente.html')

def actualizar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        cliente.nombre = request.POST.get('nombre')
        cliente.apellido = request.POST.get('apellido')
        cliente.email = request.POST.get('email')
        cliente.telefono = request.POST.get('telefono')
        cliente.direccion = request.POST.get('direccion')
        cliente.save()
        return redirect('ver_clientes')
    context = {'cliente': cliente}
    return render(request, 'cliente/actualizar_cliente.html', context)

def borrar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        cliente.delete()
        return redirect('ver_clientes')
    context = {'cliente': cliente}
    return render(request, 'cliente/borrar_cliente.html', context)

# ==========================================
# FUNCIONES CRUD PARA MASCOTAS
# ==========================================

def ver_mascotas(request):
    mascotas = Mascota.objects.select_related('cliente').all().order_by('nombre')
    context = {'mascotas': mascotas}
    return render(request, 'mascota/ver_mascotas.html', context)

def agregar_mascota(request):
    clientes = Cliente.objects.all().order_by('apellido', 'nombre')
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        especie = request.POST.get('especie')
        raza = request.POST.get('raza')
        tipo = request.POST.get('tipo')
        fecha_nac = request.POST.get('fecha_nac')
        cliente_id = request.POST.get('cliente')

        if nombre and especie and cliente_id:
            cliente = get_object_or_404(Cliente, pk=cliente_id)
            Mascota.objects.create(nombre=nombre, especie=especie, raza=raza, tipo=tipo, fecha_nac=fecha_nac, cliente=cliente)
            return redirect('ver_mascotas')
        else:
            context = {'error': 'Por favor, completa todos los campos obligatorios.', 'clientes': clientes}
            return render(request, 'mascota/agregar_mascota.html', context)
    context = {'clientes': clientes}
    return render(request, 'mascota/agregar_mascota.html', context)

def actualizar_mascota(request, pk):
    mascota = get_object_or_404(Mascota, pk=pk)
    clientes = Cliente.objects.all().order_by('apellido', 'nombre')
    if request.method == 'POST':
        mascota.nombre = request.POST.get('nombre')
        mascota.especie = request.POST.get('especie')
        mascota.raza = request.POST.get('raza')
        mascota.tipo = request.POST.get('tipo')
        mascota.fecha_nac = request.POST.get('fecha_nac')
        cliente_id = request.POST.get('cliente')

        if cliente_id:
            mascota.cliente = get_object_or_404(Cliente, pk=cliente_id)
        mascota.save()
        return redirect('ver_mascotas')
    context = {'mascota': mascota, 'clientes': clientes}
    return render(request, 'mascota/actualizar_mascota.html', context)

def borrar_mascota(request, pk):
    mascota = get_object_or_404(Mascota, pk=pk)
    if request.method == 'POST':
        mascota.delete()
        return redirect('ver_mascotas')
    context = {'mascota': mascota}
    return render(request, 'mascota/borrar_mascota.html', context)

# ==========================================
# FUNCIONES CRUD PARA PRODUCTOS
# ==========================================

CATEGORIAS_PRODUCTO = [
    'Alimento', 'Juguetes', 'Accesorios', 'Cuidado e Higiene',
    'Camas y Descanso', 'Ropa', 'Entrenamiento', 'Salud'
]

def ver_productos(request):
    productos = Producto.objects.all().order_by('nombre_producto')
    context = {'productos': productos}
    return render(request, 'producto/ver_productos.html', context)

def agregar_producto(request):
    if request.method == 'POST':
        nombre_producto = request.POST.get('nombre_producto')
        descripcion = request.POST.get('descripcion')
        categoria = request.POST.get('categoria')
        precio = request.POST.get('precio')
        stock = request.POST.get('stock')

        if nombre_producto and categoria and precio and stock:
            Producto.objects.create(
                nombre_producto=nombre_producto,
                descripcion=descripcion,
                categoria=categoria,
                precio=precio,
                stock=stock
            )
            return redirect('ver_productos')
        else:
            context = {
                'error': 'Por favor, completa todos los campos obligatorios.',
                'categorias': CATEGORIAS_PRODUCTO
            }
            return render(request, 'producto/agregar_producto.html', context)

    context = {
        'categorias': CATEGORIAS_PRODUCTO
    }
    return render(request, 'producto/agregar_producto.html', context)

def actualizar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.nombre_producto = request.POST.get('nombre_producto')
        producto.descripcion = request.POST.get('descripcion')
        producto.categoria = request.POST.get('categoria')
        producto.precio = request.POST.get('precio')
        producto.stock = request.POST.get('stock')
        producto.save()
        return redirect('ver_productos')

    context = {
        'producto': producto,
        'categorias': CATEGORIAS_PRODUCTO
    }
    return render(request, 'producto/actualizar_producto.html', context)

def borrar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.delete()
        return redirect('ver_productos')
    context = {'producto': producto}
    return render(request, 'producto/borrar_producto.html', context)

# ==========================================
# FUNCIONES CRUD PARA SERVICIOS
# ==========================================

CATEGORIAS_SERVICIO = [
    'Peluquería', 'Consulta Veterinaria', 'Vacunación', 'Desparasitación',
    'Guardería', 'Entrenamiento', 'Baño y Corte', 'Chequeo General'
]

def ver_servicios(request):
    servicios = Servicio.objects.all().order_by('nombre_servicio')
    context = {'servicios': servicios}
    return render(request, 'servicio/ver_servicios.html', context)

def agregar_servicio(request):
    if request.method == 'POST':
        nombre_servicio = request.POST.get('nombre_servicio')
        descripcion = request.POST.get('descripcion')
        duracion_min = request.POST.get('duracion_min')
        precio = request.POST.get('precio')
        categoria = request.POST.get('categoria')

        if nombre_servicio and duracion_min and precio and categoria:
            Servicio.objects.create(
                nombre_servicio=nombre_servicio,
                descripcion=descripcion,
                duracion_min=duracion_min,
                precio=precio,
                categoria=categoria
            )
            return redirect('ver_servicios')
        else:
            context = {
                'error': 'Por favor, completa todos los campos obligatorios.',
                'categorias': CATEGORIAS_SERVICIO
            }
            return render(request, 'servicio/agregar_servicio.html', context)
    
    context = {
        'categorias': CATEGORIAS_SERVICIO
    }
    return render(request, 'servicio/agregar_servicio.html', context)

def actualizar_servicio(request, pk):
    servicio = get_object_or_404(Servicio, pk=pk)
    if request.method == 'POST':
        servicio.nombre_servicio = request.POST.get('nombre_servicio')
        servicio.descripcion = request.POST.get('descripcion')
        servicio.duracion_min = request.POST.get('duracion_min')
        servicio.precio = request.POST.get('precio')
        servicio.categoria = request.POST.get('categoria')
        servicio.save()
        return redirect('ver_servicios')

    context = {
        'servicio': servicio,
        'categorias': CATEGORIAS_SERVICIO
    }
    return render(request, 'servicio/actualizar_servicio.html', context)

def borrar_servicio(request, pk):
    servicio = get_object_or_404(Servicio, pk=pk)
    if request.method == 'POST':
        servicio.delete()
        return redirect('ver_servicios')
    context = {'servicio': servicio}
    return render(request, 'servicio/borrar_servicio.html', context)

# ==========================================
# FUNCIONES CRUD PARA VETERINARIOS
# ==========================================

ESPECIALIDADES_VETERINARIO = [
    'General', 'Cirugía', 'Dermatología', 'Oftalmología',
    'Cardiología', 'Nutrición', 'Comportamiento', 'Exóticos'
]

def ver_veterinarios(request):
    veterinarios = Veterinario.objects.all().order_by('apellido', 'nombre')
    context = {'veterinarios': veterinarios}
    return render(request, 'veterinario/ver_veterinarios.html', context)

def agregar_veterinario(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        licencia = request.POST.get('licencia')
        telefono = request.POST.get('telefono')
        especialidad = request.POST.get('especialidad')

        if nombre and apellido and licencia:
            Veterinario.objects.create(
                nombre=nombre, apellido=apellido, licencia=licencia,
                telefono=telefono, especialidad=especialidad
            )
            return redirect('ver_veterinarios')
        else:
            context = {
                'error': 'Por favor, completa todos los campos obligatorios.',
                'especialidades': ESPECIALIDADES_VETERINARIO
            }
            return render(request, 'veterinario/agregar_veterinario.html', context)
    
    context = {
        'especialidades': ESPECIALIDADES_VETERINARIO
    }
    return render(request, 'veterinario/agregar_veterinario.html', context)

def actualizar_veterinario(request, pk):
    veterinario = get_object_or_404(Veterinario, pk=pk)
    if request.method == 'POST':
        veterinario.nombre = request.POST.get('nombre')
        veterinario.apellido = request.POST.get('apellido')
        veterinario.licencia = request.POST.get('licencia')
        veterinario.telefono = request.POST.get('telefono')
        veterinario.especialidad = request.POST.get('especialidad')
        veterinario.save()
        return redirect('ver_veterinarios')

    context = {
        'veterinario': veterinario,
        'especialidades': ESPECIALIDADES_VETERINARIO
    }
    return render(request, 'veterinario/actualizar_veterinario.html', context)

def borrar_veterinario(request, pk):
    veterinario = get_object_or_404(Veterinario, pk=pk)
    if request.method == 'POST':
        veterinario.delete()
        return redirect('ver_veterinarios')
    context = {'veterinario': veterinario}
    return render(request, 'veterinario/borrar_veterinario.html', context)

# ==========================================
# FUNCIONES CRUD PARA CITAS (Muchos a Muchos)
# ==========================================

def ver_citas(request):
    citas = Cita.objects.select_related('cliente', 'servicio', 'veterinario').all().order_by('-fecha_cita', '-hora_cita')
    context = {'citas': citas}
    return render(request, 'cita/ver_citas.html', context)

def agregar_cita(request):
    clientes = Cliente.objects.all().order_by('apellido', 'nombre')
    servicios = Servicio.objects.all().order_by('nombre_servicio')
    veterinarios = Veterinario.objects.all().order_by('apellido', 'nombre')

    if request.method == 'POST':
        cliente_id = request.POST.get('cliente')
        servicio_id = request.POST.get('servicio')
        veterinario_id = request.POST.get('veterinario')
        fecha_cita = request.POST.get('fecha_cita')
        hora_cita = request.POST.get('hora_cita')
        notas = request.POST.get('notas')

        if cliente_id and servicio_id and fecha_cita and hora_cita:
            cliente = get_object_or_404(Cliente, pk=cliente_id)
            servicio = get_object_or_404(Servicio, pk=servicio_id)
            veterinario = get_object_or_404(Veterinario, pk=veterinario_id) if veterinario_id else None

            # Validación adicional para evitar citas duplicadas (ya manejada por unique_together en el modelo)
            # Pero podemos dar un feedback más amigable si lo detectamos aquí
            if Cita.objects.filter(cliente=cliente, servicio=servicio, fecha_cita=fecha_cita, hora_cita=hora_cita).exists():
                context = {
                    'error': 'Ya existe una cita para este cliente y servicio en la misma fecha y hora.',
                    'clientes': clientes,
                    'servicios': servicios,
                    'veterinarios': veterinarios,
                    'valores_post': request.POST # Para pre-llenar el formulario
                }
                return render(request, 'cita/agregar_cita.html', context)

            Cita.objects.create(
                cliente=cliente,
                servicio=servicio,
                veterinario=veterinario,
                fecha_cita=fecha_cita,
                hora_cita=hora_cita,
                notas=notas
            )
            return redirect('ver_citas')
        else:
            context = {
                'error': 'Por favor, completa todos los campos obligatorios.',
                'clientes': clientes,
                'servicios': servicios,
                'veterinarios': veterinarios,
                'valores_post': request.POST
            }
            return render(request, 'cita/agregar_cita.html', context)
    
    context = {
        'clientes': clientes,
        'servicios': servicios,
        'veterinarios': veterinarios,
        'valores_post': {} # Para la primera carga del formulario
    }
    return render(request, 'cita/agregar_cita.html', context)


def actualizar_cita(request, pk):
    cita = get_object_or_404(Cita, pk=pk)
    clientes = Cliente.objects.all().order_by('apellido', 'nombre')
    servicios = Servicio.objects.all().order_by('nombre_servicio')
    veterinarios = Veterinario.objects.all().order_by('apellido', 'nombre')

    if request.method == 'POST':
        cliente_id = request.POST.get('cliente')
        servicio_id = request.POST.get('servicio')
        veterinario_id = request.POST.get('veterinario')
        fecha_cita_str = request.POST.get('fecha_cita')
        hora_cita_str = request.POST.get('hora_cita')
        notas = request.POST.get('notas')

        if cliente_id and servicio_id and fecha_cita_str and hora_cita_str:
            cliente = get_object_or_404(Cliente, pk=cliente_id)
            servicio = get_object_or_404(Servicio, pk=servicio_id)
            veterinario = get_object_or_404(Veterinario, pk=veterinario_id) if veterinario_id else None

            # Comprobar si la nueva combinación cliente, servicio, fecha, hora ya existe en otra cita
            if Cita.objects.filter(
                cliente=cliente,
                servicio=servicio,
                fecha_cita=fecha_cita_str,
                hora_cita=hora_cita_str
            ).exclude(pk=cita.pk).exists():
                context = {
                    'error': 'Ya existe otra cita para este cliente y servicio en la misma fecha y hora.',
                    'cita': cita,
                    'clientes': clientes,
                    'servicios': servicios,
                    'veterinarios': veterinarios
                }
                return render(request, 'cita/actualizar_cita.html', context)

            cita.cliente = cliente
            cita.servicio = servicio
            cita.veterinario = veterinario
            cita.fecha_cita = fecha_cita_str
            cita.hora_cita = hora_cita_str
            cita.notas = notas
            cita.save()
            return redirect('ver_citas')
        else:
            context = {
                'error': 'Por favor, completa todos los campos obligatorios.',
                'cita': cita,
                'clientes': clientes,
                'servicios': servicios,
                'veterinarios': veterinarios
            }
            return render(request, 'cita/actualizar_cita.html', context)
    
    # Formatear la fecha y hora para los campos de input HTML
    cita.fecha_cita_formatted = cita.fecha_cita.isoformat()
    cita.hora_cita_formatted = cita.hora_cita.strftime('%H:%M')

    context = {
        'cita': cita,
        'clientes': clientes,
        'servicios': servicios,
        'veterinarios': veterinarios
    }
    return render(request, 'cita/actualizar_cita.html', context)


def borrar_cita(request, pk):
    cita = get_object_or_404(Cita, pk=pk)
    if request.method == 'POST':
        cita.delete()
        return redirect('ver_citas')
    context = {'cita': cita}
    return render(request, 'cita/borrar_cita.html', context)