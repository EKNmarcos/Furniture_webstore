# Generated by Django 5.0.6 on 2024-06-11 06:09

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_furniture_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='updated_at',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='category',
            name='descripcion',
            field=models.CharField(blank=True, default='', help_text='Características adicionales del mueble.', null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='nombre',
            field=models.CharField(choices=[(1, 'Mesa'), (2, 'Silla'), (3, 'Cama'), (4, 'Comedor'), (5, 'Jardín'), (6, 'Escritorio')], default='Mesa', help_text='(silla, mesa...)'),
        ),
    ]