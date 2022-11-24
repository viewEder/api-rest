from django.shortcuts import render

# Librerias de rest framework:
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
# Serializador de datos:
from core import serializadores

# Create your views here.
class ProductoView(viewsets.ViewSet):
    """ Test de Validación """

    serial_class = serializadores.ProductoSerializer

    # Métodos:
    def list(self, request):
        diccionario = {
            'productos': self.serial_class
        }
        return Response(diccionario)
