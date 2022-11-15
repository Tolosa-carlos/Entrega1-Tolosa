from django.shortcuts import render
from app_mvt.models import *
from app_mvt.forms import EmpleadosForm, MenuForm
# Create your views here.


def inicio(request):
    return render(request, "app_mvt/base.html")

def menu(request):
    return render(request, "app_mvt/menu.html")

def busqueda_menu(request):
    return render(request, "app_mvt/menu_busqueda.html")

def resultado_busqueda_menu(request):

    nombre_menu = request.GET["nombre_menu"]
    menu = Menu.objects.filter(nombre__icontains=nombre_menu)

    return render(request, "app_mvt/menu_resultado_busqueda.html", {"menu": menu})

def crear_menu(request):

    if request.method == "POST":
        formulario = MenuForm(request.POST)

        if formulario.is_valid():

            data = formulario.cleaned_data

            menu = Menu(nombre = data["nombre"], precio=data["precio"])
            menu.save()

    formulario = EmpleadosForm()

    contexto = {"formulario": formulario}

    return render(request, "app_mvt/menu_formulario.html", contexto)

def empleados(request):
    return render(request, "app_mvt/empleado.html")

def busqueda_empleados(request):
    return render(request, "app_mvt/empleado_busqueda.html")

def resultado_busqueda_empleados(request):

    nombre_empleado = request.GET["nombre_empleado"]
    empleado = Empleados.objects.filter(nombre__icontains=nombre_empleado)

    return render(request, "app_mvt/empleado_resultado_busqueda.html", {"empleado": empleado})

def nuevo_empleado(request):

    if request.method == "POST":
        formulario = EmpleadosForm(request.POST)

        if formulario.is_valid():

            data = formulario.cleaned_data

            empleado = Empleados(nombre = data["nombre"], apellido=data["apellido"], edad=data["edad"])
            empleado.save()

    formulario = EmpleadosForm()

    contexto = {"formulario": formulario}

    return render(request, "app_mvt/empleado_formulario.html", contexto)

    