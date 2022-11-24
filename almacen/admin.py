from django.contrib import admin
from .models import Categoria, SubCategoria, Producto

class CategoriaAdmin(admin.ModelAdmin):
    pass

class SubCategoriaAdmin(admin.ModelAdmin):
    list_display = ['categoria', 'nombre_subcategoria']
    list_display_links = ['categoria', 'nombre_subcategoria']
    read_only_field = ('create_at', 'modify_at')

class ProductoAdmin(admin.ModelAdmin):
    list_display = ['subcategoria', 'nombre_producto', 'valor_venta', 'disponibilidad']
    list_display_links = ['subcategoria', 'nombre_producto']
    read_only_field = ('create_at', 'modify_at')

# Register your models here.
admin.site.register(Categoria)
admin.site.register(SubCategoria, SubCategoriaAdmin)
admin.site.register(Producto, ProductoAdmin)