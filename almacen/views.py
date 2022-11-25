from django.shortcuts import render

# Librerias de rest framework:
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
# Serializador de datos:
from core import serializadores
# Modelo de Datos:
from .models import Producto

# Create your views here.
class ProductoView(viewsets.ModelViewSet):
    """ Test de Validación """
    # Renombrar el atributo serializer_class
    serializer_class = serializadores.ProductoSerializer
    # Consulta a la base de datos
    queryset = Producto.objects.all()
