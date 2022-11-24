from django.contrib import admin
from .models import GenderUser, User

# Configurar como se ve el modelo:
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'genero', 'last_login', 'is_staff')
    ordering = ('id', 'genero')


# Register your models here.
admin.site.register(GenderUser)
admin.site.register(User, UserAdmin)