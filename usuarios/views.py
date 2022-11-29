from django.shortcuts import render

# Librerias de rest_framework:
from rest_framework.response import Response
from rest_framework import status, filters
from rest_framework.authentication import TokenAuthentication
from rest_framework import viewsets

# Importamos los permisos desde core:
from core import permissions, serializadores

# Librerias necesarias para login:
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

# Importamos el modelo de datos:
from usuarios.models import User

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    """ Creación y edición de usuario """
    # Renombrar el atributo serializer_class
    serializer_class = serializadores.UserSerializer
    # Consulta a la base de datos
    queryset = User.objects.all()
    # Autenticadoresde usuario:
    authentication_classes = (TokenAuthentication,)
    # Activación de permisos:
    permission_classes = (permissions.UpdateOwnProfile,)
    # Activar motor de búsqueda:
    filter_backends = (filters.SearchFilter,)
    # Campos a buscar:
    search_fields = ('username', 'email',)


class UserLoginView(ObtainAuthToken):
    """ Administrar tokens de usuario """
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
