## Proyecto coder - Preentrega 

### Como ingresar a los urls?

* Ingresar a la url "mvt/" y luego ingresar a una de las siguentes rutas:

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
    path("servicios/", servicios, name="app-servicios"),
    path("servicios/buscar/", busqueda_servicios, name="app-servicios-buscar"),
    path("servicios/buscar/resultados/", resultado_busqueda_servicios, name="app-servicios-buscar-resultados"),
    path("servicios/crear/", nuevo_servicio, name="app-nuevo-servicio"),
    
]


## Funciones

- Se pueden registrar personas, servicios y comidas, tambien se pueden buscar a los mismos.
