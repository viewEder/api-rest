# Importar librerias de rutas
from django.urls import path, include
# Importar vistas
from .views import ProductoView
# Manejo de rutas de rest_framework =
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('catalogo', ProductoView, basename='catalogo')

urlpatterns = [
    path('', include(router.urls)),
]

# urlpatterns += router.urls