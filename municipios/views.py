from django.shortcuts import render
from municipios.models import ONG, Entidad_reguladora, Municipio
# Create your views here.


def index_municipio(request):
    mun = Municipio.objects.all()
    count = mun.count()
    data = {'title': 'Municipios', 'data' : mun, 'count' : count}
    return render(request, 'municipio/index.html', data)

def ongs(request):
    ong = ONG.objects.all()
    count = ong.count()
    data = {'title': 'Municipios', 'data' : ong, 'count' : count}
    return render(request, 'municipio/ong.html', data)

def entidades(request):
    ent = Entidad_reguladora.objects.all()
    count = ent.count()
    data = {'title': 'Municipios', 'data' : ent, 'count' : count}
    return render(request, 'municipio/entidades.html', data)