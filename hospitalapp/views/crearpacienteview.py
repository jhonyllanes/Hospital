from email.policy import HTTP
from urllib import request
from rest_framework import status, views
from rest_framework.response import Response

from hospitalapp.serializers.pacienteserializer import PacienteSerializer

class CrearPacienteView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializar=PacienteSerializer(data=request.data)
        if serializar.is_valid():
            serializar.save()
            return Response(serializar.data,status=status.HTTP_201_CREATED)
        return Response(serializar.errors, status=status.HTTP_400_BAD_REQUEST)