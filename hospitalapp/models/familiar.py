from django.db import models
from .Usuario import Usuario
from .paciente import Paciente

class Familiar(models.Model):
    id_familiar = models.AutoField(primary_key=True)
    username = models.ForeignKey(Usuario, related_name='Familiar', on_delete=models.CASCADE)
    id_paciente = models.ForeignKey(Paciente, related_name='Familiar', on_delete=models.CASCADE)
    parentesco = models.CharField('Parentesco', max_length = 35)
    correo = models.EmailField('Correo', max_length = 120)