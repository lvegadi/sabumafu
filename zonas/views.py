from django.shortcuts import render

# Importar modelos
from zonas.models import Zona_protegida

# Create your views here.
def index(request):
    data = {'title': 'sabumafu'}
    return render(request,'zonas/index.html',data)

def zona(request,id):
    myzona = Zona_protegida.objects.filter(id=id).first()
    data = {'title' : myzona.nombre, 'zona' : myzona}
    return render(request,'zonas/zona.html',data)    

def todazona(request):
    data = {'title' : 'zonas protegidas'}
    return render(request,'zonas/todas.html',data)  