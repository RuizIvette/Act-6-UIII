from django.db import models

# Create your models here.
# ==========================================
# MODELO: Cliente
# ==========================================
class Cliente(models.Model):
    cliente_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    direccion = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

# ==========================================
# MODELO: Mascota
# ==========================================
class Mascota(models.Model):
    mascota_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    especie = models.CharField(max_length=50) # Ej: Perro, Gato, Ave
    raza = models.CharField(max_length=50, blank=True, null=True) # Ej: Labrador, Siamés
    tipo = models.CharField(max_length=50, blank=True, null=True) # Ej: Doméstica, Exótica
    fecha_nac = models.DateField(blank=True, null=True)
    # Conexión con el modelo Cliente (Un cliente puede tener muchas mascotas)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='mascotas')

    def __str__(self):
        return f"{self.nombre} ({self.especie}) - Dueño: {self.cliente.nombre} {self.cliente.apellido}"

# ==========================================
# MODELO: Producto
# ==========================================
class Producto(models.Model):
    producto_id = models.AutoField(primary_key=True)
    nombre_producto = models.CharField(max_length=100)
    categoria = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre_producto} ({self.categoria})"

# ==========================================
# MODELO: Servicio
# ==========================================
class Servicio(models.Model):
    servicio_id = models.AutoField(primary_key=True)
    nombre_servicio = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    duracion_min = models.IntegerField(default=30)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.CharField(max_length=50) # Ej: Peluquería, Consulta Veterinaria, Entrenamiento

    def __str__(self):
        return f"{self.nombre_servicio} ({self.categoria})"

# ==========================================
# MODELO: Veterinario
# ==========================================
class Veterinario(models.Model):
    veterinario_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    licencia = models.CharField(max_length=50, unique=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    especialidad = models.CharField(max_length=100, blank=True, null=True) # Ej: Cirugía, Dermatología

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.especialidad})"

# ==========================================
# MODELO: Cita (Muchos a Muchos entre Cliente y Servicio)
# ==========================================
class Cita(models.Model):
    cita_id = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='citas')
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE, related_name='citas')
    veterinario = models.ForeignKey(Veterinario, on_delete=models.SET_NULL, null=True, blank=True, related_name='citas_asignadas')
    fecha_cita = models.DateField()
    hora_cita = models.TimeField()
    notas = models.TextField(blank=True, null=True)

    class Meta:
        # Asegura que un cliente no pueda tener dos citas para el mismo servicio a la misma hora y fecha
        unique_together = ('cliente', 'servicio', 'fecha_cita', 'hora_cita')

    def __str__(self):
        return f"Cita {self.cita_id} - Cliente: {self.cliente.apellido} ({self.fecha_cita} {self.hora_cita})"