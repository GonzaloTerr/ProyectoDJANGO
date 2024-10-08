from django.db import models
from django.utils import timezone
from thumbnails.fields import ImageField
from ckeditor.fields import RichTextField
# Create your models here.

class Course (models.Model):
    title=models.CharField(verbose_name= "Titulo del curso", max_length=200)
    content=RichTextField(verbose_name= "Contenido del curso")
    create_at=models.DateTimeField(verbose_name= "Fecha y hora de creacion",default=timezone.now)
    call_link=models.URLField(verbose_name= "Enlace de llamada")
    show_home=models.BooleanField("Mostrar en la home", default=False)
    toc=models.FileField(verbose_name="Temario",upload_to="courses/toc/",null=True,blank=True)
    course_images=ImageField(verbose_name="Portada del curso",upload_to="courses/images/",null=True,blank=True)
    def __str__(self):
        return self.title
