from django.db import models

# Create your models here.

class Entidad_reguladora(models.Model):
    nombre = models.CharField(max_length=45)
    telefono = models.CharField(max_length=20)
    correo = models.EmailField(max_length=60)
    def __str__(self):
        return self.nombre;

class ONG(models.Model):
    nombre = models.CharField(max_length=45)
    tipo = models.CharField(max_length=45)
    telefono = models.CharField(max_length=20)
    correo = models.EmailField(max_length=60)
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