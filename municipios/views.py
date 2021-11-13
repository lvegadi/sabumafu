from django.shortcuts import render
from municipios.models import Municipio
# Create your views here.


def index_municipio(request):
    mun = Municipio.objects.all()
    count = mun.count()
    data = {'title': 'Municipios', 'data' : mun, 'count' : count}
    return render(request, 'municipio/index.html', data)
