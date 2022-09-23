from hospitalapp.models import sig_vitales
from hospitalapp.models.sig_vitales import Signos_Vitales
from rest_framework import serializers

class SignosVitalesSerializer(serializers.ModelSerializer):
    class Meta:
        model=sig_vitales
        fields=('username','Osimetria','Frecuencia_Respiratoria','Frecuencia_Cardiaca','Temperatura','Presion_Arterial ','Glicemias','Fecha_Registro')