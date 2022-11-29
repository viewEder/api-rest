""" Configuración de ruta """
# Importar librerias de rutas
from django.urls import path, include
# Importar vistas
from .views import UserViewSet, UserLoginView
# Manejo de rutas de rest_framework =
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('usuarios', UserViewSet)

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('', include(router.urls)),
]

# urlpatterns += router.urls