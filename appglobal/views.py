
from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from .forms import *


def index(request):
    return render(request ,"inicio.html")

def pinturas(request):
    return render(request ,"cargar_pinturas.html")

def accesorios(request):
    return render(request ,"cargar_accesorios.html")

def clientes(request):
    form = ClientesForm()
    condiciones = Clientes.CONDICIONES
    context = {'form': form, 'condiciones': condiciones}
    return render(request, 'cargar_clientes.html', context)



def cargar_pintura(request):
    if request.method == 'POST':
        form = PinturasForm(request.POST)
        if form.is_valid():
            form.save()
            print("Datos guardados correctamente")
        else:
            print(form.errors)
    else:
        form = PinturasForm()
    return render(request, 'pintura_cargada.html', {'form': form})

def cargar_accesorios(request):
    if request.method == 'POST':
        form = AccesoriosForm(request.POST)
        if form.is_valid():
            form.save()
            print("Datos guardados correctamente")
        else:
            print(form.errors)
    else:
        form = AccesoriosForm()
    return render(request, 'accesorio_cargado.html', {'form': form})

def cargar_clientes(request):
    if request.method == 'POST':
        form = ClientesForm(request.POST)
        if form.is_valid():
            form.save()
            print("Datos guardados correctamente")
        else:
            print(form.errors)
    else:
        form = ClientesForm()
    return render(request, 'cliente_cargado.html', {'form': form})

def mostrar_clientes(request):
     clientes = Clientes.objects.all()  # Obtener todos los clientes
     return render(request, 'mostrar_clientes.html', {'clientes': clientes})

def mostrar_pinturas(request):
     pinturas = Pinturas.objects.all() 
     return render(request, 'mostrar_pinturas.html', {'pinturas': pinturas})

def mostrar_accesorios(request):
    accesorios = Accesorios.objects.all()
    return render(request, 'mostrar_accesorios.html',{'accesorios': accesorios})

def buscar_pinturas(request):
    resultados = None
    query = request.GET.get('q')
    if query:
        resultados = Pinturas.objects.filter(name__icontains=query)
    return render(request, 'buscar_pinturas.html', {'resultados': resultados, 'query': query})


