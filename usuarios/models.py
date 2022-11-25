from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.contrib.auth.models import BaseUserManager, PermissionsMixin
from django.db.models import CASCADE
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class GenderUser(models.Model):
    genero = models.CharField(verbose_name="Género", max_length=20)
    # Atributos de Auditoria:
    create_at = models.DateField(auto_now = False, auto_now_add = True, verbose_name = "Fecha de creación", null = True, blank = True) 
    modify_at = models.DateField(auto_now = True, auto_now_add = False, verbose_name = "Fecha de actualización", null = True, blank = True)

    class Meta:
        verbose_name_plural = 'Generos'
    
    def __str__(self):
        return f'{self.genero}'

class UserManager(BaseUserManager):
    """ Administrador de Usuario """
    def create_user(self, email, username, password=None):
        # Validación para que el usuario ingrese el email:
        if not email:
            raise ValueError('El correo electrónico es obligatorio')
        
        # Construir el objeto con los paramétros ingresados:
        email = self.normalize_email(email)                     # Dar formato al texto ingresado al campo email
        user = self.model(email=email, username=username)
        user.set_password(password)
        user.save(using = self._db)

        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(email, username, password)

        user.is_staff = True
        user.is_superuser = True
        user.save(using = self._db)

        return user


class User(AbstractUser, PermissionsMixin):
    # Sobrescribo los atributos de la clase User:
    email = models.EmailField(max_length = 255, unique = True)
    username = models.CharField(verbose_name = 'Username', max_length=25, null=True, blank=True)
    is_staff = models.BooleanField(default = False)
    is_active = models.BooleanField(default = True)
    is_superuser = models.BooleanField(default = False)
    # Atributos adicionales:
    birthday = models.DateField(auto_now = False, verbose_name = "Fecha de Nacimiento", null = True, blank = True)
    genero = models.ForeignKey(GenderUser, on_delete=CASCADE, null = True, blank = True)
    biografia = models.TextField(verbose_name = "Biografía", null = True, blank = True)
    link = models.URLField(verbose_name = "Link personal", max_length = 200, null = True, blank = True)

    # Defino la creación de usuarios usando la clase UserManager():
    objects = UserManager()
    
    # Defino commo constante obligatoria:
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    # Creamos el método string para devolver el usuario:
    def __str__(self):
        return f'{self.username}'

# Función decorador:
@receiver(post_save, sender=User)
def ensure_profile_exist(sender, instance, **kwargs):
    if kwargs.get('created', False):
        User.objects.get_or_create(username=instance)