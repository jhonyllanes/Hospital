from django.db import models
from .Usuario import Usuario

class Personal_Salud(models.Model):
    id_salud = models.AutoField(primary_key=True)
    username = models.ForeignKey(Usuario, related_name='Psalud', on_delete=models.CASCADE)
    rol = models.CharField('Rol', max_length = 35)
    especialidad = models.CharField('Especialidad', max_length = 35)