from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Region(models.Model):
    id_region = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f'{self.nombre}'


class Comuna(models.Model):
    id_comuna = models.BigAutoField(primary_key=True)
    id_region = models.ForeignKey(Region, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f'{self.nombre}'

class TipoInmueble(models.Model):
    id_tipo = models.BigAutoField(primary_key=True)
    tipo_inmueble = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f'{self.tipo_inmueble}'

class Usuario(AbstractUser):
    confirm_password = models.CharField(max_length=100)
    description = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
    
    def __str__(self):
        return f"{self.username}"

    def get_complete_name(self):
        return f"{self.first_name} {self.last_name}"

class Inmueble(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    m2_construidos = models.FloatField()
    m2_totales = models.FloatField()
    estacionamientos = models.IntegerField()
    habitaciones = models.IntegerField()
    banos = models.IntegerField()
    direccion = models.CharField(max_length=200)
    precio_mensual = models.DecimalField(max_digits=10, decimal_places=2)
    eliminada = models.BooleanField(default=False)
    id_region = models.ForeignKey(Region, on_delete=models.CASCADE)
    id_comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)
    id_tipo = models.ForeignKey(TipoInmueble, on_delete=models.CASCADE)
    id_propietario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Inmueble'
        verbose_name_plural = 'Inmuebles'

    def __str__(self):
        return self.nombre
"""
class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    
    password1 = models.CharField(max_length=100)
    password2 = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    imagen_perfil = models.ImageField(null=True,verbose_name='Imagen de perfil',blank=True)
"""
"""
class Arrendador(models.Model):
    usuario = models.CharField(max_length=100)
    password1 = models.CharField(max_length=100)
    password2 = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

class Arrendatario(models.Model):
    usuario = models.CharField(max_length=100)
    password1 = models.CharField(max_length=100)
    password2 = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
"""