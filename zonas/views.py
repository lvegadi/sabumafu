from django.shortcuts import render
from django.http import Http404
# Importar modelos
from zonas.models import Fauna, Flora, Zona_protegida, Flora_zona, Fauna_zona
from zonas.forms import UserRegister
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    data = {'title': 'sabumafu'}
    return render(request, 'zonas/index.html', data)


def registro(request):
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request,f'Usuario {username} creado')
    else:
            form = UserRegister()
    data = {'data' : form}
    return render(request, 'ingreso/registro.html', data)


def zona(request, slug=None):
    if slug is not None:
        try:
            myzona = Zona_protegida.objects.get(slug=slug)
        except Zona_protegida.DoesNotExist:
            raise Http404
        except:
            raise Http404
    data = {'title': myzona.nombre, 'zona': myzona , 'flora': myzona.id}
    return render(request, 'zonas/zona.html', data)


def todazona(request):
    lista = Zona_protegida.objects.all()
    count = lista.count()
    data = {'title': 'zonas protegidas', 'count': count, 'lista': lista}
    return render(request, 'zonas/todas.html', data)


def flora(request, id=None):
    if id is not None:
        try:
            flora = Flora_zona.objects.filter(zona=id)
        except Flora_zona.DoesNotExist:
            raise Http404
        except:
            raise Http404
    data = {'flora': flora}
    return render(request, 'flora/index.html', data)

def todaflora(request):
    lista = Flora.objects.all()
    count = lista.count()
    data = {'title': 'Flora', 'count': count, 'flora': lista}
    return render(request, 'flora/index.html', data)

def fauna(request, id=None):
    if id is not None:
        try:
            fauna = Fauna_zona.objects.filter(zona=id)
        except Fauna_zona.DoesNotExist:
            raise Http404
        except:
            raise Http404
    data = {'fauna': fauna}
    return render(request, 'fauna/index.html', data)

def todafauna(request):
    lista = Fauna.objects.all()
    count = lista.count()
    data = {'title': 'Fauna', 'count': count, 'fauna': lista}
    return render(request, 'fauna/index.html', data)

@login_required(login_url='/account/login/')
def alerta(request):
    data = {'title': 'sabumafu'}
    return render(request, 'alerta/index.html', data)
