from django.db import models

# Create your models here.
class Persona(models.Model):
    rut = models.IntegerField(db_column='rut', blank=False)
    nombre = models.TextField(db_column='nombre', blank=False, max_length=20)
    apellido = models.TextField(db_column='apellido', blank=False, max_length=30)