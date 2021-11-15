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
from zonas.views import index, zona, todazona, registro, flora, todaflora, fauna, todafauna, alerta, report, alerta_pdf
from municipios.views import index_municipio
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
    path('alerta/', alerta, name="alert"),
    path('reporte/', report, name="report"),
    #-- MUNICIPIOS --#
    path('municipio/', index_municipio, name="index_municipio"),

    #Reportes.
    path('zonas', alerta_pdf, name='alerta-pdf'),



]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)