# Generated by Django 5.1 on 2024-08-13 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_autor_alter_post_content_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='show_home',
            field=models.BooleanField(default=False, verbose_name='Mostrar en la home'),
        ),
    ]