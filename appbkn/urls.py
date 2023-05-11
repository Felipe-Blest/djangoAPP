from . import views
from django.urls import path

urlpatterns = [    
    path('listaPersona', views.PersonaList, name='lista-persona'),
    path('crearPersona/', views.CrearPersona, name='crear-persona'),
    path('persona-modif/<int:id>', views.ActualizarPersona, name='modif-persona'),
    path('persona-borrar/<int:id>', views.EliminarPersona, name='borrar-persona'),
]
