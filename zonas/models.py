from django.db import models
from django.db.models.signals import pre_save, post_save
from municipios.models import Municipio
from .utils import slugify_instance_title
import pathlib
import uuid
# Create your models here.

#subir imagenes
def image_upload_handler(instance, filename):
    fpath = pathlib.Path(filename)
    new_fname = str(uuid.uuid1())
    path = instance.__class__.__name__
    return f"images/{path}/{new_fname}{fpath.suffix}"

def geojson_upload_handler(instance, filename):
    fpath = pathlib.Path(filename)
    new_fname = str(uuid.uuid1())
    return f"geojson/{new_fname}{fpath.suffix}"


class Zona_protegida(models.Model):
    nombre = models.CharField(max_length=45)
    descripcion = models.TextField()
    caracteristicas = models.TextField()
    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE, null=True, blank=True)
    latitud = models.DecimalField(max_digits=20, decimal_places=10)
    longitud = models.DecimalField(max_digits=20, decimal_places=10)
    geojson = models.FileField(upload_to=geojson_upload_handler, blank=True, null=True)
    image = models.ImageField(upload_to=image_upload_handler, blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)

    # def save(self, *args, **kwargs):
    #    if self.slug is None:
    #         self.slug = slugify(self.nombre)
    #    super().save(*args, **kwargs)
    def __str__(self):
        return self.nombre


class Alerta(models.Model):
    tipo_alerta = models.CharField(max_length=30)
    usuario = models.DecimalField(max_digits=10, decimal_places=0)
    fecha = models.DateField()
    zona = models.ForeignKey(
        Zona_protegida, on_delete=models.CASCADE, blank=True, null=True)


class Fauna(models.Model):
    nombre = models.CharField(max_length=45)
    especie = models.CharField(max_length=45)
    image = models.ImageField(upload_to=image_upload_handler, blank=True, null=True)
    descripcion = models.TextField()
    def __str__(self):
        return self.nombre + " " + self.especie

class Flora(models.Model):
    nombre = models.CharField(max_length=45)
    especie = models.CharField(max_length=45)
    image = models.ImageField(upload_to=image_upload_handler, blank=True, null=True)
    descripcion = models.TextField()
    def __str__(self):
        return self.nombre + " " + self.especie


class Fauna_zona(models.Model):
    poblacion = models.DecimalField(max_digits=10, decimal_places=0)
    observaciones = models.TextField()
    fauna = models.ForeignKey(
        Fauna, on_delete=models.CASCADE, null=True, blank=True)
    zona = models.ForeignKey(
        Zona_protegida, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.fauna.nombre + " en " + self.zona.nombre



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
