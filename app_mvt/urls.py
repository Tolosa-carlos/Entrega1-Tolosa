from django.urls import path
from app_mvt.views import *

urlpatterns = [
    path("", inicio, name="app-inicio"),
    path("menu/", menu, name="app-menu"),
    path("menu/buscar/", busqueda_menu, name="app-menu-buscar"),
    path("menu/buscar/resultados/", resultado_busqueda_menu, name="app-menu-buscar-resultados"),
    path("menu/crear/", crear_menu, name="app-crear-menu"),
    path("empleados/", empleados, name="app-empleados"),
    path("empleados/buscar/", busqueda_empleados, name="app-empleados-buscar"),
    path("empleados/buscar/resultados", resultado_busqueda_empleados, name="app-empleados-buscar-resultados"),
    path("empleados/cargar/", nuevo_empleado, name="app-nuevos-empleados"),



]