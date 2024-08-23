from django.db import models
from django.utils import timezone

# Create your models here.

class Contact (models.Model):
    nombre=models.CharField(verbose_name="Nombre",max_length=140)
    email=models.EmailField(verbose_name="Email")
    comentario=models.TextField(verbose_name="Comentario en la web")
    create_at=models.DateTimeField(verbose_name= "Fecha y hora de creacion",default=timezone.now)
    contactado=models.BooleanField(verbose_name="Ya me contacté", default=False)
    def __str__(self):
        return self.nombre