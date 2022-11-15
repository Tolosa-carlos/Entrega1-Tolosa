from django.shortcuts import render
from app_mvt.models import *
from app_mvt.forms import *
# Create your views here.


def inicio(request):
    return render(request, "app_mvt/index.html")

def story(request):
    return render(request, "app_mvt/story.html")

def menu(request):
    return render(request, "app_mvt/menu.html")

def busqueda_menu(request):
    return render(request, "app_mvt/busqueda_menu.html")

def resultado_busqueda_menu(request):

    nombre_menu = request.GET["nombre_menu"]
    menu = Menu.objects.filter(menu__icontains=nombre_menu)

    return render(request, "app_mvt/resultados_busqueda_menu.html", {"menu": menu})

def crear_menu(request):

    if request == "POST":
        formulario = MenuForm(request.POST)

        if not formulario.is_valid():
            
            data = formulario.cleaned_data
            menu = Menu(nombre = data["nombre"], clase = data["clase"], precio = ["precio"])
            menu.save()
            
            return render(request, "app_mvt/base.html")
        


    formulario = MenuForm()
    contexto = {"formulario": formulario}

    return render(request, "app_mvt/menu_formulario.html", contexto)

    