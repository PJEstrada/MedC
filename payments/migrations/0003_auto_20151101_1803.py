# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0002_auto_20151101_1611'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='detalles',
            field=models.TextField(default='Ninguno', max_length=10000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='invoice',
            name='insurance',
            field=models.CharField(choices=[('Ninguno', 'Ninguno'), ('G&T', 'G&T'), ('El Roble', 'El Roble'), ('La Ceiba', 'La Ceiba'), ('Aseguradora Generali', 'La Ceiba')], max_length=255),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='items',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Consulta', 'Consulta'), ('Inyeccion', 'Inyeccion'), ('Medicamentos', 'Medicamentos'), ('Examen', 'Examen')], max_length=255),
        ),
    ]
