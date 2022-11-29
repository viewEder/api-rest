# importamos librerias
from rest_framework import permissions

# 
class UpdateOwnProfile(permissions.BasePermission):
    """ Clase para que el usuario logueado pueda modificar su perfil o sus datos: """
    def has_object_permission(self, request, view, obj):
        # Validar si el usuario tiene los permisos adecuados para ejecutar métodos:
        if request.method in permissions.SAFE_METHODS:
            # Métodos que se pueden ejecutar en un formulario:
            return True
        
        return obj.id == request.user.id # Retorno true o false