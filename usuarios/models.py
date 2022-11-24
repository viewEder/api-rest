from django.db import models
from django.contrib.auth.models import AbstractUser
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

class User(AbstractUser):
    birthday = models.DateField(auto_now = False, verbose_name = "Fecha de Nacimiento", null = True, blank = True)
    genero = models.ForeignKey(GenderUser, on_delete=CASCADE, null = True, blank = True)
    biografia = models.TextField(verbose_name = "Biografía", null = True, blank = True)
    link = models.URLField(verbose_name = "Link personal", max_length = 200, null = True, blank = True)

# Función decorador:
@receiver(post_save, sender=User)
def ensure_profile_exist(sender, instance, **kwargs):
    if kwargs.get('created', False):
        User.objects.get_or_create(username=instance)