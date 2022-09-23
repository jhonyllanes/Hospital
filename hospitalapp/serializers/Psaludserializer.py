from hospitalapp.models.Psalud import Personal_Salud
from rest_framework import serializers

class PersonalSaludSerializer(serializers.ModelSerializer):
    class Meta:
        model=Personal_Salud
        fields=('username','rol','especialidad')