from django.shortcuts import render
from django.http import Http404

# librerias PDF
from io import BytesIO
from django import template
from django.http.response import HttpResponse
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.utils import timezone

# Importar modelos
from zonas.models import Alerta, Fauna, Flora, Zona_protegida, Flora_zona, Fauna_zona, Flora_poblacion, Fauna_poblacion
from municipios.models import Departamento, Municipio, ONG_municipio, ONG
from zonas.forms import UserRegister
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Permission, User
import os
from datetime import datetime
# Create your views here.
# sirve mitimiti


def index(request):
    alert = Alerta.objects.all().order_by('-id')[:5]
    #last = list(alert)
    #last = last[-5:]
    data = {'title': 'Sabumafu', 'alert': alert}
    return render(request, 'zonas/index.html', data)
# sirve

def about(request):
    data = {'title': 'Sabumafu'}
    return render(request, 'zonas/about.html', data)
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
    data = {'data': form}
    return render(request, 'ingreso/registro.html', data)
# sirve


def zona(request, slug=None):
    if slug is not None:
        try:
            myzona = Zona_protegida.objects.get(slug=slug)
        except Zona_protegida.DoesNotExist:
            raise Http404
        except:
            raise Http404
    data = {'title': myzona.nombre, 'zona': myzona, 'id': myzona.id}

    return render(request, 'zonas/zona.html', data)
# editar


def todazona(request):
    lista = Zona_protegida.objects.all()
    count = lista.count()
    data = {'title': 'Zonas protegidas', 'count': count, 'lista': lista}
    return render(request, 'zonas/todas.html', data)
# sirve


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
# sirve


def todaflora(request):
    lista = Flora.objects.all()
    count = lista.count()
    data = {'title': 'Flora', 'count': count, 'flora': lista}
    return render(request, 'flora/index.html', data)
# sirve


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
# sirve


def todafauna(request):
    lista = Fauna.objects.all()
    count = lista.count()
    data = {'title': 'Fauna', 'count': count, 'fauna': lista}
    return render(request, 'fauna/index.html', data)


def detail_flora(request,id=None):
    if id is not None:
        try:
            f = Flora.objects.get(id=id)
            f_zona = Flora_zona.objects.get(flora_id=f.id)
        except Flora.DoesNotExist:
            raise Http404
        except:
            raise Http404
    data = {'flora': f, 'flora_z': f_zona}
    return render(request, 'flora/detalle.html', data)

def detail_fauna(request,id=None):
    if id is not None:
        try:
            f = Fauna.objects.get(id=id)
            f_zona = Fauna_zona.objects.get(fauna_id=f.id)
        except Fauna.DoesNotExist:
            raise Http404
        except:
            raise Http404
    data = {'fauna': f, 'fauna_z': f_zona}
    return render(request, 'fauna/detalle.html', data)
# Dashboard


@login_required(login_url='/account/login/')  # sirve
def alerta(request):
    zona = Zona_protegida.objects.all()
    now = datetime.now()
    date = str(now.year) + "-" + str(now.month) + "-" + str(now.day)
    if request.method == 'POST':
        alert_type = request.POST.get('slc_lrt_tp')
        user = request.POST.get('slc_user')
        user1 = User.objects.get(id=user)
        zone = request.POST.get('slc_zone')
        zone_id = Zona_protegida.objects.get(slug=zone)
        a = Alerta(tipo_alerta=alert_type, usuario=user1, fecha=date, zona=zone_id)
        a.save()
    data = {'title': 'Alerta', 'zona': zona, 'date': date}
    return render(request, 'alerta/index.html', data)

@login_required(login_url='/account/login/')  # sirve
def configure(request):
    if request.method == 'POST':
        actual_user = User.objects.get(id = request.POST.get('conf_id'))
        if request.POST.get('conf_email') != "":
            actual_user.email = request.POST.get('conf_email')
            actual_user.save()
            messages.success(request, 'Email actualizado satisfactoriamente.')
        if request.POST.get('conf_name') != "":
            actual_user.first_name = request.POST.get('conf_name')
            actual_user.save()
            messages.success(request, 'Nombre actualizado satisfactoriamente.')
        if request.POST.get('conf_lst_name') != "":
            actual_user.last_name = request.POST.get('conf_lst_name')
            actual_user.save()
            messages.success(request, 'Apellido actualizado satisfactoriamente.')
        if request.POST.get('conf_usernm') != "":
            actual_user.username = request.POST.get('conf_usernm')
            actual_user.save()
            messages.success(request, 'Username actualizado satisfactoriamente.')
        if request.POST.get('conf_pss') != "" and request.POST.get('conf_pss1') != "":
            print(request.POST.get('conf_pass'))
            print(request.POST.get('conf_pass1'))
            if request.POST.get('conf_pass')==(request.POST.get('conf_pass1')): 
                actual_user.set_password(request.POST.get('conf_pss'))
                actual_user.save()
                messages.success(request, 'Contrase??a actualizada satisfactoriamente.')
            else:
                messages.success(request, 'Contrase??a NO actualizada.')

        #user = request.POST.get('slc_user')
        #user1 = User.objects.get(id=user)
        #zone = request.POST.get('slc_zone')
        #zone_id = Zona_protegida.objects.get(slug=zone)
        #a = Alerta()
    data = {'title': 'Alerta'}
    return render(request, 'configuracion/index.html', data)

@login_required(login_url='/account/login/')
def dashboard(request):
    data = {'title': 'Dashboard'}
    return render(request, 'reportes/index.html', data)

# Reportes


@login_required(login_url='/account/login/')
def reportes(request):
    data = {'title': 'Reportes'}
    return render(request, 'reportes/reportes.html', data)


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
        zone = (request.POST.get('zona'))
        if request.POST.get('fecha_inicio') :
            inicio = request.POST.get('fecha_inicio')
        else:
            inicio = '2001-01-01'
        if request.POST.get('fecha_fin') :
            fin = request.POST.get('fecha_fin')
        else:
            fin = '2999-12-31'
        print(inicio, "AAAAA ", fin)
        alerta = Alerta.objects.select_related('usuario','zona').filter(zona_id = zone, fecha__range=[inicio, fin])
        myzona = Zona_protegida.objects.get(id=zone)
        username = request.user.username
        now = timezone.now()
        data = {'alerta': alerta, 'user': username,
                'fecha': now, 'myzona': myzona}
        pdf = render_to_pdf('reportes/pdf_alerta.html', data)
        return HttpResponse(pdf, content_type='application/pdf')

    lista = Zona_protegida.objects.all().order_by('nombre')
    data = {'title': 'Reporte de filtros', 'lista': lista}
    return render(request, 'reportes/reporte1.html', data)

# Reporte 2
@login_required(login_url='/account/login/')
def reporte_fauna(request):
    if request.method == 'POST':

        zone = (request.POST.get('zona'))
        fauna = Fauna.objects.raw('SELECT zonas_fauna.id, zonas_fauna.nombre, zonas_fauna.especie, zonas_fauna.descripcion, zonas_fauna_zona.observaciones, zonas_fauna_zona.id as zonaid FROM zonas_fauna, zonas_fauna_zona where zonas_fauna.id = zonas_fauna_zona.fauna_id   and zonas_fauna_zona.zona_id =' + zone)
        myzona = Zona_protegida.objects.get(id=zone)

        poblacion = []
        # Por cada fauna_zona se busca la poblacion historica
        for pobfauna in fauna:
            zonpob = (Fauna_poblacion.objects.filter(fauna=pobfauna.zonaid))
            if zonpob.count() > 0:
                for rowpob in zonpob:
                    poblacion.append({'id': rowpob.id, 'poblacion_historica': str(
                        rowpob.poblacion_historica), 'fecha': rowpob.fecha, 'fauna_id': rowpob.fauna_id})

        username = request.user.username
        now = timezone.now()
        data = {'fauna': fauna, 'poblacion': poblacion,
                'user': username, 'fecha': now, 'myzona': myzona}
        pdf = render_to_pdf('reportes/pdf_fauna.html', data)
        return HttpResponse(pdf, content_type='application/pdf')

    lista = Zona_protegida.objects.all().order_by('nombre')
    data = {'title': 'Reporte de filtros', 'lista': lista}
    return render(request, 'reportes/reporte2.html', data)


# Reporte 3
@login_required(login_url='/account/login/')
def reporte_flora(request):
    if request.method == 'POST':
        poblacion = []
        zone = (request.POST.get('zona'))
        flora = Flora.objects.raw('SELECT zonas_flora.id, zonas_flora.nombre, zonas_flora.especie, zonas_flora.descripcion, zonas_flora_zona.observaciones, zonas_flora_zona.id as zonaid FROM zonas_flora, zonas_flora_zona where zonas_flora.id = zonas_flora_zona.flora_id   and zonas_flora_zona.zona_id =' + zone)
        myzona = Zona_protegida.objects.get(id=zone)

        poblacion = []
        # Por cada flora_zona se busca la poblacion historica
        for pobflora in flora:
            zonpob = (Flora_poblacion.objects.filter(flora=pobflora.zonaid))
            if zonpob.count() > 0:
                for rowpob in zonpob:
                    poblacion.append({'id': rowpob.id, 'poblacion_historica': str(
                        rowpob.poblacion_historica), 'fecha': rowpob.fecha, 'flora_id': rowpob.flora_id})

        #poblacion = (Flora_poblacion.objects.filter(flora=zone))

        username = request.user.username
        now = timezone.now()
        data = {'flora': flora, 'poblacion': poblacion,
                'user': username, 'fecha': now, 'myzona': myzona}
        pdf = render_to_pdf('reportes/pdf_flora.html', data)
        return HttpResponse(pdf, content_type='application/pdf')

    lista = Zona_protegida.objects.all().order_by('nombre')
    data = {'title': 'Reporte de filtros', 'lista': lista}
    return render(request, 'reportes/reporte3.html', data)


# Reporte 4
@login_required(login_url='/account/login/')
def reporte_dpto(request):
    if request.method == 'POST':
        dpto = (request.POST.get('dpto'))
        mydpto = Departamento.objects.get(id=dpto)

        municipios = []
        zonas_protegidas = []

        # Se filtran todos los municipios del departamento seleccionado
        query_municipios = (Municipio.objects.select_related(
            'departamento').filter(departamento_id=dpto))

        # Se recorren para buscar las solo las ONGs asociados y municip??os que contengan informaci??n.
        for rowmun in query_municipios:
            zonpro = (Zona_protegida.objects.filter(municipio=rowmun.id))
            if zonpro.count() > 0:
                municipios.append(
                    {'id': rowmun.id, 'codigo': rowmun.codigo, 'nombre': rowmun.nombre})
                for rowpro in zonpro:
                    zonas_protegidas.append({'id': rowpro.id, 'municipio_id': rowpro.municipio_id, 'nombre': rowpro.nombre,
                                            'latitud': rowpro.latitud, 'longitud': rowpro.longitud, 'descripcion': rowpro.descripcion, 'slug': rowpro.slug})

        username = request.user.username
        now = timezone.now()
        data = {'municipios': municipios, 'zonas_protegidas': zonas_protegidas,
                'user': username, 'fecha': now, 'mydpto': mydpto}
        pdf = render_to_pdf('reportes/pdf_dpto.html', data)
        return HttpResponse(pdf, content_type='application/pdf')

    lista = Departamento.objects.all().order_by('nombre')
    data = {'title': 'Reporte de filtros', 'lista': lista}
    return render(request, 'reportes/reporte4.html', data)

# Reporte 5


@login_required(login_url='/account/login/')
def reporte_ong(request):
    if request.method == 'POST':
        dpto = (request.POST.get('dpto'))
        mydpto = Departamento.objects.get(id=dpto)
        todas_ong = []
        todos_municipios = []

        # Se filtran todos los municipios del departamento seleccionado
        query_municipios = (Municipio.objects.select_related(
            'departamento').filter(departamento_id=dpto))

        # Se recorren para buscar las solo las ONGs asociados y municip??os que contengan informaci??n.
        for rowmun in query_municipios:
            ongmun = (ONG_municipio.objects.filter(municipio=rowmun.id))
            if ongmun.count() > 0:
                todos_municipios.append(
                    {'id': rowmun.id, 'codigo': rowmun.codigo, 'nombre': rowmun.nombre})
                for rowong in ongmun:
                    ong = ONG.objects.get(id=rowong.ong_id)
                    todas_ong.append({'id': rowong.id, 'municipio_id': rowong.municipio_id, 'nombre': ong.nombre,
                                     'tipo': ong.tipo, 'correo': ong.correo, 'image': ong.image, 'telefono': ong.telefono})

        username = request.user.username
        now = timezone.now()
        data = {'todos_municipios': todos_municipios, 'todas_ong': todas_ong,
                'user': username, 'fecha': now, 'mydpto': mydpto}
        pdf = render_to_pdf('reportes/pdf_ong.html', data)
        return HttpResponse(pdf, content_type='application/pdf')

    lista = Departamento.objects.all().order_by('nombre')
    data = {'title': 'Reporte de filtros', 'lista': lista}
    return render(request, 'reportes/reporte5.html', data)
