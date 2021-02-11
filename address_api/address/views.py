from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import AddressSerializer
from .models import Address
from rest_framework import status
from rest_framework.views import APIView
import json
import requests


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all().order_by('id')
    serializer_class = AddressSerializer
    http_method_names = ['get', 'put', 'delete']


class AddressApi(APIView):
    def post(self, request):
        serializer = AddressSerializer(data=request.data)
        if serializer.is_valid():
            rqst = requests.get(f"https://viacep.com.br/ws/{serializer.validated_data['cep']}/json")
            result = json.loads(rqst.content)
            if result:
                serializer.validated_data['cep'] = result['cep']
                serializer.validated_data['street'] = result['logradouro']
                serializer.validated_data['district'] = result['bairro']
                serializer.validated_data['city'] = result['localidade']
                serializer.validated_data['state'] = result['uf']

            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
