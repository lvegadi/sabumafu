from django.contrib import admin
from municipios.models import Entidad_reguladora, Entidad_municipio,  ONG_municipio, Municipio, Departamento, ONG

# Register your models here.

admin.site.register(Municipio)
admin.site.register(Departamento)
admin.site.register(Entidad_reguladora)
admin.site.register(ONG)
admin.site.register(Entidad_municipio)
admin.site.register(ONG_municipio)


