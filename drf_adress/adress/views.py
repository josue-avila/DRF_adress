from rest_framework import viewsets
from rest_framework import status 
from rest_framework.views import APIView 
from rest_framework.response import Response 
from .serializers import AdressSerializer
from .models import Adress
import requests
import json


class AdressViewSet(viewsets.ModelViewSet):
    queryset = Adress.objects.all().order_by('cep')
    serializer_class = AdressSerializer


class AdressApi(APIView):
    def post(self, request):
        serializer = AdressSerializer(data=request.data)
        if serializer.is_valid():
            rqst = requests.get(f"https://viacep.com.br/ws/{serializer['cep']}/json")
            result = rqst.json()
            if result:
                serializer.data['cep'] = result['cep']
                serializer.data['street'] = result['logradouro']
                serializer.data['district'] = result['bairro']
                serializer.data['city'] = result['localidade']
                serializer.data['state'] = result['uf']

            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
