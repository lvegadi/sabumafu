from django.db import models
from municipios.models import Municipio
# Create your models here.
class Zona_protegida(models.Model):
    nombre = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=200)
    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE, null=True, blank=True)
    coordenada_x = models.DecimalField(max_digits=20, decimal_places=10)
    coordenada_y = models.DecimalField(max_digits=20, decimal_places=10)
    geojson_url = models.CharField(max_length=60)

class Alerta(models.Model):
    tipo_alerta = models.CharField(max_length=30)
    usuario_id = models.DecimalField(max_digits=10)
    fecha = models.DateField()
    zona = models.ForeignKey(Zona_protegida, on_delete=models.CASCADE, blank=True, null=True)
    
class Fauna(models.Model):
    nombre = models.CharField(max_length=45)
    especie = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=200)

class Flora(models.Model):
    nombre = models.CharField(max_length=45)
    especie = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=200)

class Fauna_zona(models.Model):
    poblacion = models.DecimalField(max_digits=10)
    observaciones = models.CharField(max_length=200)
    fauna = models.ForeignKey(Fauna, on_delete=models.CASCADE, null=True, blank=True)
    zona = models.ForeignKey(Zona_protegida, on_delete=models.CASCADE, null=True, blank=True)

class Flora_zona(models.Model):
    poblacion = models.DecimalField(max_digits=10)
    observaciones = models.CharField(max_length=200)
    fauna = models.ForeignKey(Fauna, on_delete=models.CASCADE, null=True, blank=True)
    zona = models.ForeignKey(Zona_protegida, on_delete=models.CASCADE, null=True, blank=True)