# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Personas
from .models import Galguerias
from .models import Preferecias_galguerias
from .forms import PersonaForm
from .forms import GalgueriaForm
from .forms import PreferenciaForm
from .forms import SignUpForm
from django.shortcuts import redirect
from django.contrib.auth import login, authenticate


def index(request):
    latest_galguerias_list = Galguerias.objects.order_by('nombre_producto', 'tipo', 'cantidad_producto')
    context = {'latest_galguerias_list': latest_galguerias_list}
    return render(request, 'monoku/listar_galgerias.html', context)


def galgueria(request):
    galgueria = Galguerias.objects.all()
    #  context = {'galgueria': galgueria.values('nombre_producto')}
    return HttpResponse(galgueria.values('nombre_producto', 'tipo', 'cantidad_producto'))


def crear_galguerias(request):
    if request.method == "POST":
        form = GalgueriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('http://127.0.0.1:8000/monoku/')
    else:
        form = GalgueriaForm()
    context = {
        'form': form
    }
    return render(request, 'monoku/crear_galguerias.html', context)


def personas(request):
    latest_personas_list = Personas.objects.order_by('nombre_persona', 'edad', 'cargo')
    template = loader.get_template('monoku/personas.html')
    context = {
        'latest_personas_list': latest_personas_list,
    }
    return HttpResponse(template.render(context, request))


def crear_personas(request):
    if request.method == "POST":
        form = PersonaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('monoku:personas')
    else:
        form = PersonaForm()
    context = {
        'form': form
    }
    return render(request, 'monoku/crear_personas.html', context)


def preferencias_galguerias(request):
    latest_preferencias_list = Preferecias_galguerias.objects.order_by('persona','producto', 'cantidad_consumido', 'fecha')
    template = loader.get_template('monoku/preferencias.html')
    context = {
        'latest_preferencias_list': latest_preferencias_list,
    }
    return HttpResponse(template.render(context, request))


def crear_preferencias(request):
    if request.method == "POST":
        form = PreferenciaForm(request.POST)
        if form.is_valid():
            print (form)
            cantidad = form['cantidad_consumido'].value()
            id_galgueria = form['producto'].value()
            seleccion = Galguerias.objects.get(pk=id_galgueria)
            consumo = seleccion.cantidad_producto - int(cantidad)
            seleccion.cantidad_producto = consumo
            seleccion.save()
            form.save()
            return redirect('http://127.0.0.1:8000/monoku/')
    else:
        form = PreferenciaForm()
    context = {
        'form': form
    }
    return render(request, 'monoku/crear_preferencias.html', context)


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            print (form)
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('http://127.0.0.1:8000/admin')
    else:
        form = SignUpForm()
    return render(request, 'monoku/signup.html', {'form': form})
