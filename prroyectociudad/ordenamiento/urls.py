from django.urls import path
# se importa las vistas de la aplicación
from . import views

urlpatterns = [
        path('', views.index, name='index'),
        path('parroquia/<int:id>', views.obtener_parroquia, 
            name='obtener_parroquia'),
        path('crear/parroquia', views.crear_parroquia, 
            name='crear_parroquia'),
        path('editar_parroquia/<int:id>', views.editar_parroquia, 
            name='editar_parroquia'),
        # numeros telefonicos
        path('crear/barrio', views.crear_barrio, 
            name='crear_barrio'),
        path('editar/barrio/<int:id>', views.editar_barrio, 
            name='editar_barrio'),
 ]