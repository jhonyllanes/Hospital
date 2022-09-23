from django.db import models
from .Usuario import Usuario
from .Psalud import Personal_Salud


class Paciente(models.Model):
    id_paciente = models.AutoField(primary_key=True)
    id_Psalud = models.ForeignKey(Personal_Salud, related_name='Psalud', on_delete=models.CASCADE)
    username = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    direccion = models.CharField('Direccion', max_length = 80)
    ciudad = models.CharField('Ciudad', max_length = 35)
    fecha_nacimiento = models.DateField()