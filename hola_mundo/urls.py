
from django.contrib import admin
from django.urls import path
from hola.views import def_hola, def_login, def_articulo, def_articulos,def_articulo_eliminar
from hola.views import def_articulo_editar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hola/', def_hola),
    path('login/', def_login),
    path('articulo/', def_articulo, name='articulo'),
    path('articulos/', def_articulos, name='articulos'),
    path('articulo-eliminar/<int:id>', def_articulo_eliminar, name='eliminar'),
    path('articulo-editar/<int:id>', def_articulo_editar, name='editar'),
]
