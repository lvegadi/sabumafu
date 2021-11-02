from django.contrib import admin
from zonas.models import Zona_protegida, Alerta, Flora, Fauna, Flora_zona, Fauna_zona

# Register your models here.
admin.site.register(Alerta)
admin.site.register(Zona_protegida)
admin.site.register(Fauna)
admin.site.register(Fauna_zona)
admin.site.register(Flora)
admin.site.register(Flora_zona)

