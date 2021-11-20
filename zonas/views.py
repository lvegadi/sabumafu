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
from municipios.models import Departamento, Municipio, ONG_municipio, ONG
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

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)

    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='aplication/pdf')
    return None


# Reporte 1
@login_required(login_url='/account/login/')
def reporte_alerta(request):
    if request.method == 'POST':
       zone =  (request.POST.get('zona'))
       alerta =  Alerta.objects.raw( 'select zonas_alerta.id, zonas_alerta.tipo_alerta, zonas_alerta.usuario, zonas_alerta.fecha, zonas_zona_protegida.nombre, auth_user.username from zonas_alerta inner join zonas_zona_protegida on zonas_alerta.zona_id=zonas_zona_protegida.id inner join auth_user on auth_user.id=zonas_alerta.usuario where zonas_zona_protegida.id=' + zone  )
       if request.POST.get('fecha_inicio'):
           print('creado')
       myzona = Zona_protegida.objects.get(id=zone)
       username = request.user.username
       now = timezone.now()
       data = {'alerta': alerta,'user':username,'fecha':now, 'myzona':myzona}
       pdf = render_to_pdf('reportes/pdf_alerta.html', data)
       return HttpResponse(pdf, content_type='application/pdf')


    lista = Zona_protegida.objects.all()
    data = {'title': 'Reporte de filtros', 'lista': lista}
    return render(request, 'reportes/reporte1.html', data)    

# Reporte 2
@login_required(login_url='/account/login/')
def reporte_fauna(request):
    if request.method == 'POST':
       zone =  (request.POST.get('zona'))
       fauna = Fauna.objects.raw('SELECT zonas_fauna.id, zonas_fauna.nombre, zonas_fauna.especie, zonas_fauna.descripcion, zonas_fauna_zona.observaciones FROM zonas_fauna, zonas_fauna_zona where zonas_fauna.id = zonas_fauna_zona.fauna_id   and zonas_fauna_zona.zona_id =' + zone  )
       myzona = Zona_protegida.objects.get(id=zone)
       username = request.user.username
       now = timezone.now()
       data = {'fauna': fauna,'user':username,'fecha':now, 'myzona':myzona}
       pdf = render_to_pdf('reportes/pdf_fauna.html', data)
       return HttpResponse(pdf, content_type='application/pdf')
    #NO sirvio de esta manera
    # if request.method == 'POST':
    #    zone =  (request.POST.get('zona'))
    #    myzona = Zona_protegida.objects.get(id=zone)
   
    #    fauna = []

    #    queryzonas = (Fauna_zona.objects.filter(zona=zone))
    #    if queryzonas.count() > 0:
    #         for rowzonas in queryzonas:
    #             faunaquery = (Fauna.objects.get(fauna=rowzonas.fauna))
    #             fauna.append({'id':faunaquery.id,'nombre':faunaquery.nombre,'especies':faunaquery.especies,'descripcion':faunaquery.descripcion,'image':faunaquery.image})


    lista = Zona_protegida.objects.all()
    data = {'title': 'Reporte de filtros', 'lista': lista}
    return render(request, 'reportes/reporte2.html', data)    


# Reporte 3
@login_required(login_url='/account/login/')
def reporte_flora(request):
    if request.method == 'POST':
       zone =  (request.POST.get('zona'))
       flora = Flora.objects.raw('SELECT zonas_flora.id, zonas_flora.nombre, zonas_flora.especie, zonas_flora.descripcion, zonas_flora_zona.observaciones FROM zonas_flora, zonas_flora_zona where zonas_flora.id = zonas_flora_zona.flora_id   and zonas_flora_zona.zona_id =' + zone  )
       myzona = Zona_protegida.objects.get(id=zone)
       username = request.user.username
       now = timezone.now()
       data = {'flora': flora,'user':username,'fecha':now, 'myzona':myzona}
       pdf = render_to_pdf('reportes/pdf_flora.html', data)
       return HttpResponse(pdf, content_type='application/pdf')
    
    #No sirvio de esta manera
    # if request.method == 'POST':
    #    zone =  (request.POST.get('zona'))
    #    myzona = Zona_protegida.objects.get(id=zone)
    #    flora = []

    #    queryzonas = (Flora_zona.objects.filter(zona=zone))
    #    if queryzonas.count() > 0:
    #         for rowzonas in queryzonas:
    #             floraquery = (Flora.objects.get(flora=rowzonas.flora))
    #             flora.append({'id':floraquery.id,'nombre':floraquery.nombre,'especies':floraquery.especies,'descripcion':floraquery.descripcion,'image':floraquery.image})


    lista = Zona_protegida.objects.all()
    data = {'title': 'Reporte de filtros', 'lista': lista}
    return render(request, 'reportes/reporte3.html', data)    


# Reporte 4
@login_required(login_url='/account/login/')
def reporte_dpto(request):
    if request.method == 'POST':
       dpto =  (request.POST.get('dpto'))
       mydpto = Departamento.objects.get(id=dpto)

       municipios = []
       zonas_protegidas = []

       #Se filtran todos los municipios del departamento seleccionado
       query_municipios = (Municipio.objects.select_related('departamento').filter(departamento_id=dpto))

       #Se recorren para buscar las solo las ONGs asociados y municipíos que contengan información.
       for rowmun in query_municipios:
           zonpro = (Zona_protegida.objects.filter(municipio=rowmun.id))
           if zonpro.count() > 0:
              municipios.append({'id':rowmun.id,'codigo':rowmun.codigo,'nombre':rowmun.nombre} )
              for rowpro in zonpro:
                  zonas_protegidas.append({'id':rowpro.id,'municipio_id':rowpro.municipio_id,'nombre':rowpro.nombre,'latitud':rowpro.latitud,'longitud':rowpro.longitud,'descripcion':rowpro.descripcion, 'slug':rowpro.slug})

      
  
       username = request.user.username
       now = timezone.now()
       data = {'municipios': municipios,'zonas_protegidas': zonas_protegidas,'user':username,'fecha':now, 'mydpto':mydpto}
       pdf = render_to_pdf('reportes/pdf_dpto.html', data)
       return HttpResponse(pdf, content_type='application/pdf')


    lista = Departamento.objects.all()
    data = {'title': 'Reporte de filtros', 'lista': lista}
    return render(request, 'reportes/reporte4.html', data)    

# Reporte 5
@login_required(login_url='/account/login/')
def reporte_ong(request):
    if request.method == 'POST':
       dpto =  (request.POST.get('dpto'))
       mydpto = Departamento.objects.get(id=dpto)
       todas_ong = []
       todos_municipios = []

       #Se filtran todos los municipios del departamento seleccionado
       query_municipios = (Municipio.objects.select_related('departamento').filter(departamento_id=dpto))

       #Se recorren para buscar las solo las ONGs asociados y municipíos que contengan información.
       for rowmun in query_municipios:
           ongmun = (ONG_municipio.objects.filter(municipio=rowmun.id))
           if ongmun.count() > 0:
              todos_municipios.append({'id':rowmun.id,'codigo':rowmun.codigo,'nombre':rowmun.nombre} )
              for rowong in ongmun:
                  ong = ONG.objects.get(id=rowong.ong_id)
                  todas_ong.append({'id':rowong.id,'municipio_id':rowong.municipio_id,'nombre':ong.nombre,'tipo':ong.tipo, 'correo':ong.correo,'image':ong.image,'telefono':ong.telefono})

      
       username = request.user.username
       now = timezone.now()
       data = {'todos_municipios': todos_municipios,'todas_ong': todas_ong,'user':username,'fecha':now, 'mydpto':mydpto}
       pdf = render_to_pdf('reportes/pdf_ong.html', data)
       return HttpResponse(pdf, content_type='application/pdf')


    lista = Departamento.objects.all()
    data = {'title': 'Reporte de filtros', 'lista': lista}
    return render(request, 'reportes/reporte5.html', data)   
