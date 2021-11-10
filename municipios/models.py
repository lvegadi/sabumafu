from django.db import models
import pathlib
import uuid

# Create your models here.

def image_upload_handler(instance, filename):
    fpath = pathlib.Path(filename)
    new_fname = str(uuid.uuid1())
    path = instance.__class__.__name__
    return f"images/{path}/{new_fname}{fpath.suffix}"

class Entidad_reguladora(models.Model):
    nombre = models.CharField(max_length=45)
    telefono = models.CharField(max_length=20)
    correo = models.EmailField(max_length=60)
    image = models.ImageField(upload_to=image_upload_handler, blank=True, null=True)
    def __str__(self):
        return self.nombre;

class ONG(models.Model):
    nombre = models.CharField(max_length=45)
    tipo = models.CharField(max_length=45)
    telefono = models.CharField(max_length=20)
    correo = models.EmailField(max_length=60)
    image = models.ImageField(upload_to=image_upload_handler, blank=True, null=True)
    def __str__(self):
        return self.nombre;

class Departamento(models.Model):
    nombre = models.CharField(max_length=45)
    def __str__(self):
        return self.nombre;

class Municipio(models.Model):
    nombre = models.CharField(max_length=45)
    codigo = models.CharField(max_length=20)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.nombre;

class Entidad_municipio(models.Model):
    entidad = models.ForeignKey(Entidad_reguladora, on_delete=models.CASCADE, null=True, blank=True)
    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE, null=True, blank=True)

class ONG_municipio(models.Model):
    ong = models.ForeignKey(ONG, on_delete=models.CASCADE, null=True, blank=True)
    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE, null=True, blank=True)    