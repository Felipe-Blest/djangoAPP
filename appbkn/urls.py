from . import views
from django.urls import path

urlpatterns = [    
    path('listaPersona', views.listaPersona, name='lista-persona'),
    path('crearPersona', views.crearPersona, name='crear-persona'),
    path('persona-modif/<int:id>', views.modifPersona, name='modif-persona'),
    path('persona-borrar/<int:id>', views.borrarPersona, name='borrar-persona'),
]