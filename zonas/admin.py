from django.contrib import admin
from zonas.models import Zona_protegida, Alerta, Flora, Fauna, Flora_zona, Fauna_zona

# Register your models here.


class Zona_protegidaAdmin(admin.ModelAdmin):
    list_display = ['id','nombre','slug','municipio','latitud','longitud']
    search_fields = ['id','nombre','descripcion']

admin.site.register(Zona_protegida,Zona_protegidaAdmin)
admin.site.register(Alerta)
admin.site.register(Fauna)
admin.site.register(Fauna_zona)
admin.site.register(Flora)
admin.site.register(Flora_zona)
