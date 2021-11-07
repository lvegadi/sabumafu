from django.db import models
from django.db.models.signals import pre_save, post_save
from municipios.models import Municipio

from .utils import slugify_instance_title

# Create your models here.


class Zona_protegida(models.Model):
    nombre = models.CharField(max_length=45)
    descripcion = models.TextField()
    caracteristicas = models.TextField()
    municipio = models.ForeignKey(
        Municipio, on_delete=models.CASCADE, null=True, blank=True)
    latitud = models.DecimalField(max_digits=20, decimal_places=10)
    longitud = models.DecimalField(max_digits=20, decimal_places=10)
    geojson_url = models.CharField(max_length=60)
    image_url = models.CharField(max_length=60)
    slug = models.SlugField(unique=True, blank=True, null=True)

    # def save(self, *args, **kwargs):
    #    if self.slug is None:
    #         self.slug = slugify(self.nombre)
    #    super().save(*args, **kwargs)
    def __str__(self):
        return self.nombre


class Alerta(models.Model):
    tipo_alerta = models.CharField(max_length=30)
    usuario_id = models.DecimalField(max_digits=10, decimal_places=0)
    fecha = models.DateField()
    zona = models.ForeignKey(
        Zona_protegida, on_delete=models.CASCADE, blank=True, null=True)


class Fauna(models.Model):
    nombre = models.CharField(max_length=45)
    especie = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=200)


class Flora(models.Model):
    nombre = models.CharField(max_length=45)
    especie = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre + " " + self.especie


class Fauna_zona(models.Model):
    poblacion = models.DecimalField(max_digits=10, decimal_places=0)
    observaciones = models.TextField()
    fauna = models.ForeignKey(
        Fauna, on_delete=models.CASCADE, null=True, blank=True)
    zona = models.ForeignKey(
        Zona_protegida, on_delete=models.CASCADE, null=True, blank=True)


class Flora_zona(models.Model):
    poblacion = models.DecimalField(max_digits=10, decimal_places=0)
    observaciones = models.TextField()
    flora = models.ForeignKey(
        Flora, on_delete=models.CASCADE, null=True, blank=True)
    zona = models.ForeignKey(
        Zona_protegida, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.flora.nombre + " en " + self.zona.nombre


class Fauna_poblacion(models.Model):
    poblacion_historica = models.DecimalField(max_digits=10, decimal_places=0)
    fecha = models.DateField()
    fauna = models.ForeignKey(
        Fauna_zona, on_delete=models.CASCADE, null=True, blank=True)


class Flora_poblacion(models.Model):
    poblacion_historica = models.DecimalField(max_digits=10, decimal_places=0)
    fecha = models.DateField()
    flora = models.ForeignKey(
        Flora_zona, on_delete=models.CASCADE, null=True, blank=True)


def zona_pre_save(sender, instance, *args, **kwargs):
    print('pre_save')
    if instance.slug is None:
        slugify_instance_title(instance, save=False)


pre_save.connect(zona_pre_save, sender=Zona_protegida)


def zona_post_save(sender, instance, created, *args, **kwargs):
    print('post_save')
    if created:
        slugify_instance_title(instance, save=True)


post_save.connect(zona_pre_save, sender=Zona_protegida)
