from . import views
from django.urls import path

urlpatterns = [    
    path('listaPersona', views.PersonaList, name='listaPersona'),
    path('crearPersona/', views.CrearPersona, name='crearPersona'),
    path('persona-modif/<int:id>', views.ActualizarPersona, name='persona-modif'),
    path('persona-borrar/<int:id>', views.EliminarPersona, name='persona-borra/'),
]
