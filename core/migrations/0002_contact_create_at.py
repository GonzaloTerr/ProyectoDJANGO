# Generated by Django 5.1 on 2024-08-23 17:46

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='create_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fecha y hora de creacion'),
        ),
    ]
