# Generated by Django 5.1 on 2024-08-13 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_course_course_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_images',
            field=models.ImageField(blank=True, null=True, upload_to='courses/images/', verbose_name='Portada del curso'),
        ),
    ]
