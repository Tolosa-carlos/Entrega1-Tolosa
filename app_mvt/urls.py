from django.urls import path
from app_mvt.views import *

urlpatterns = [
    path("", inicio, name="app-inicio"),
    path("story/", story, name="app-story"),
    path("menu/", menu, name="app-menu"),
    path("menu/buscar/", busqueda_menu, name="app-menu-buscar"),
    path("menu/buscar/resultados", busqueda_menu, name="app-menu-buscar-resultados"),
    path("menu/crear/", crear_menu, name="app-crear-menu"),



]