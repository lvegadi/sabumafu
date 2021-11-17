from django.shortcuts import render
from django.http import Http404

#librerias PDF
from io import BytesIO
from django import template
from django.http.response import HttpResponse
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.utils import timezone

# Importar modelos
from zonas.models import Alerta, Fauna, Flora, Zona_protegida, Flora_zona, Fauna_zona
from zonas.forms import UserRegister
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Permission, User
import os
from datetime import datetime
# Create your views here.
#sirve mitimiti
def index(request):
    alert = Alerta.objects.all()
    data = {'title': 'Sabumafu', 'alert' : alert}
    return render(request, 'zonas/index.html', data)
#sirve
def registro(request):
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            form.save()
            man = form.cleaned_data['username']
            messages.success(request, f'El usuario: {man} ha sido creado.')
            perm = Permission.objects.get(id=33)
            user = User.objects.get(username=man)
            user.user_permissions.add(perm)
    else:
            form = UserRegister()
    data = {'data' : form}
    return render(request, 'ingreso/registro.html', data)
#sirve
def zona(request, slug=None):
    if slug is not None:
        try:
            myzona = Zona_protegida.objects.get(slug=slug)
        except Zona_protegida.DoesNotExist:
            raise Http404
        except:
            raise Http404
    data = {'title': myzona.nombre, 'zona': myzona , 'id': myzona.id}
    
    return render(request, 'zonas/zona.html', data)
#editar
def todazona(request):
    lista = Zona_protegida.objects.all()
    count = lista.count()
    data = {'title': 'Zonas protegidas', 'count': count, 'lista': lista}
    return render(request, 'zonas/todas.html', data)
#sirve
def flora(request, id=None):
    if id is not None:
        try:
            flora = Flora_zona.objects.filter(zona=id)
        except Flora_zona.DoesNotExist:
            raise Http404
        except:
            raise Http404
    data = {'flora': flora}
    return render(request, 'flora/lista.html', data)
#sirve
def todaflora(request):
    lista = Flora.objects.all()
    count = lista.count()
    data = {'title': 'Flora', 'count': count, 'flora': lista}
    return render(request, 'flora/index.html', data)
#sirve
def fauna(request, id=None):
    if id is not None:
        try:
            fauna = Fauna_zona.objects.filter(zona=id)
        except Fauna_zona.DoesNotExist:
            raise Http404
        except:
            raise Http404
    data = {'fauna': fauna}
    return render(request, 'fauna/lista.html', data)
#sirve
def todafauna(request):
    lista = Fauna.objects.all()
    count = lista.count()
    data = {'title': 'Fauna', 'count': count, 'fauna': lista}
    return render(request, 'fauna/index.html', data)

#Dashboard

@login_required(login_url='/account/login/') #sirve
def alerta(request):
    zona = Zona_protegida.objects.all()
    now = datetime.now()
    date = str(now.year) + "-" + str(now.month) + "-" + str(now.day)
    if request.method == 'POST':
        alert_type = request.POST.get('slc_lrt_tp')
        user =  request.POST.get('slc_user')
        zone =  request.POST.get('slc_zone')
        zone_id = Zona_protegida.objects.get(slug=zone)
        a = Alerta(tipo_alerta = alert_type, usuario = user, fecha = date, zona = zone_id)
        a.save()
    data = {'title': 'Alerta', 'zona' : zona, 'date' : date}
    return render(request, 'alerta/index.html', data)

@login_required(login_url='/account/login/')
def dashboard(request):
    data = {'title': 'Dashboard'}
    return render(request,'reportes/index.html',data)  
    
# Reportes

@login_required(login_url='/account/login/')
def reportes(request):
    data = {'title': 'Reportes'}
    return render(request,'reportes/reportes.html',data)  

# Reporte 1
@login_required(login_url='/account/login/')
def reporte_alerta(request):
    if request.method == 'POST':
       zone =  (request.POST.get('zona'))
       alerta =  Alerta.objects.raw( 'select zonas_alerta.id, zonas_alerta.tipo_alerta, zonas_alerta.usuario, zonas_alerta.fecha, zonas_zona_protegida.nombre, auth_user.username from zonas_alerta inner join zonas_zona_protegida on zonas_alerta.zona_id=zonas_zona_protegida.id inner join auth_user on auth_user.id=zonas_alerta.usuario where zonas_zona_protegida.id=' + zone  )
       myzona = Zona_protegida.objects.get(id=zone)
       username = request.user.username
       now = timezone.now()
       data = {'alerta': alerta,'user':username,'fecha':now, 'myzona':myzona}
       pdf = render_to_pdf('reportes/pdf_alerta.html', data)
       return HttpResponse(pdf, content_type='application/pdf')


    lista = Zona_protegida.objects.all()
    data = {'title': 'Reporte de filtros', 'lista': lista}
    return render(request, 'reportes/reporte1.html', data)    

    
def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)

    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='aplication/pdf')
    return None







