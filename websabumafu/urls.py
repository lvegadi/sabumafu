"""websabumafu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.urls import path
from zonas.views import index, zona, todazona, registro, flora, todaflora, fauna, todafauna, alerta, dashboard,reportes,reporte_alerta, reporte_fauna, reporte_flora,  reporte_dpto, reporte_ong, configure, detail_flora, detail_fauna
from municipios.views import index_municipio, ongs, entidades
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    #-- ZONAS --#
    path('index/', index, name="index"),
    path('zonas/<slug:slug>', zona, name="zona_detalles"),
    path('zonas/', todazona, name="zona_lista"),
    path('ingreso/registro/',registro,name="signup"),
    path('flora/<int:id>',flora,name="flora"),
    path('flora/',todaflora,name="flora_lista"),
    path('fauna/<int:id>',fauna,name="fauna"),
    path('fauna/',todafauna,name="fauna_lista"),
    path('account/',include('django.contrib.auth.urls')),
    path('fauna/detalle/<int:id>', detail_fauna, name="fauna_detalles"),
    path('flora/detalle/<int:id>', detail_flora, name="flora_detalles"),

    #-- MUNICIPIOS --#
    path('municipio/', index_municipio, name="index_municipio"),
    path('ong/', ongs, name="ongs"),
    path('entidades/', entidades, name="entidades"),

    #-- DASHBOARD --#
    path('dashboard/', dashboard, name="dashboard"),
    path('dashboard/alerta/', alerta, name="alert"),
    path('dashboard/configuracion/', configure, name="config"),
    path('dashboard/reportes/', reportes, name="reportes"),
    path('dashboard/reportes/alertas', reporte_alerta, name='pdf_alerta'),
    path('dashboard/reportes/fauna', reporte_fauna, name='pdf_fauna'),
    path('dashboard/reportes/flora', reporte_flora, name='pdf_flora'),
    path('dashboard/reportes/depto', reporte_dpto, name='pdf_dpto'),
    path('dashboard/reportes/ong', reporte_ong, name='pdf_ong'),



]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
