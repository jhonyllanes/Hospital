from django.db import models
from .Usuario import Usuario

class Signos_Vitales(models.Model):
    id_registro = models.AutoField(primary_key=True)
    username = models.ForeignKey(Usuario, related_name='signos_vitales', on_delete=models.CASCADE)
    Osimetria = models.CharField('Osimetria', max_length = 10, unique=True)
    Frecuencia_Respiratoria = models.CharField('Frecuencia_Respiratoria', max_length = 15, unique=True)
    Frecuencia_Cardiaca = models.CharField('Frecuencia_Cardiaca', max_length = 15, unique=True)
    Temperatura = models.CharField('Temperatura', max_length = 15, unique=True)
    Presion_Arterial = models.CharField('Presion_Arterial', max_length = 15, unique=True)
    Glicemias = models.CharField('Glicemias', max_length = 15, unique=True)
    Fecha_Registro = models.DateTimeField()