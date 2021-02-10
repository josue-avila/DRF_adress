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
    def post(self, request, format=None):
        serializer = AdressSerializer(data=request.data)
        if serializer.is_valid():
            cep = requests.get(f"https://viacep.com.br/ws/{serialize.validated_data['cep']}/json/")
            result = json.loads(cep.content)
            if result:
                serializer.validated_data['cep'] = result['cep']
                serializer.validated_data['street'] = result['street']
                serializer.validated_data['district'] = result['district']
                serializer.validated_data['city'] = result['city']
                serializer.validated_data['state'] = result['state']
                serializer.validated_data['country'] = result['country']
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)