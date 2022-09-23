from django.db import models

from hospitalapp.models.paciente import Paciente
from .Usuario import Usuario

class Historia_Clinica(models.Model):
    
    id_historia = models.AutoField(primary_key=True)
    id_paciente = models.ForeignKey(Paciente, related_name='Historia', on_delete=models.CASCADE)
    Descripcion = models.CharField('Descripcion', max_length = 50, unique=True)
    recomendaciones = models.CharField('Recomendaciones', max_length = 20, unique=True)
   