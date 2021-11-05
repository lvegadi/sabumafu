from django.shortcuts import render
from django.http import Http404
# Importar modelos
from zonas.models import Zona_protegida

# Create your views here.
def index(request):
    data = {'title': 'sabumafu'}
    return render(request,'zonas/index.html',data)

def ingreso(request):
    data = {'title': 'sabumafu'}
    return render(request,'ingreso/index.html',data)

def zona(request,slug=None):
    if slug is not None:
        try:
           myzona = Zona_protegida.objects.get(slug=slug) 
        except:
            raise Http404
    data = {'title' : myzona.nombre, 'zona' : myzona}
    return render(request,'zonas/zona.html',data)    

def todazona(request):
    data = {'title' : 'zonas protegidas'}
    return render(request,'zonas/todas.html',data)  