from django.contrib import admin
from zonas.models import Zona_protegida, Alerta, Flora, Fauna, Flora_zona, Fauna_zona

# Register your models here.


class Zona_protegidaAdmin(admin.ModelAdmin):
    list_display = ['id','nombre','slug','municipio','latitud','longitud']
    search_fields = ['id','nombre','descripcion']

class FaunaAdmin(admin.ModelAdmin):
    list_display = ['id','nombre','especie']
    search_fields = ['id','nombre','especie']

class FloraAdmin(admin.ModelAdmin):
    list_display = ['id','nombre','especie']
    search_fields = ['id','nombre','especie']


class AlertaAdmin(admin.ModelAdmin):
    list_display = ['id','tipo_alerta','usuario','fecha','zona']
    search_fields = ['id','tipo','fecha']

admin.site.register(Zona_protegida,Zona_protegidaAdmin)
admin.site.register(Alerta,AlertaAdmin)
admin.site.register(Fauna,FaunaAdmin)
admin.site.register(Fauna_zona)
admin.site.register(Flora,FloraAdmin)
admin.site.register(Flora_zona)
