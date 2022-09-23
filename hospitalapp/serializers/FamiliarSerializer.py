from hospitalapp.models.familiar import Familiar   
from rest_framework import serializers

class familiarserializer(serializers.ModelSerializer):
    class Meta:
        model=Familiar
        fields=('username','id_paciente','parentesco','correo')