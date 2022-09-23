from hospitalapp.models import his_clinica
from hospitalapp.models.his_clinica import Historia_Clinica
from rest_framework import serializers

class historia_clinicaSerializer(serializers.ModelSerializer):
    class Meta:
        model=his_clinica
        fields=('username','Descripcion','Recomendaciones')