# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('customer_apellido', models.CharField(max_length=255)),
                ('customer_segundo_apellido', models.CharField(max_length=255)),
                ('customer_nombre', models.CharField(max_length=255)),
                ('customer_segundo_nombre', models.CharField(max_length=255)),
                ('my_field2', multiselectfield.db.fields.MultiSelectField(choices=[('Consulta', 'Consulta'), ('Inyeccion', 'Inyeccion'), ('La Ceiba', 'La Ceiba'), ('Aseguradora Generali', 'La Ceiba')], max_length=255)),
                ('items', models.CharField(choices=[('Consulta', 'Consulta'), ('Inyeccion', 'Inyeccion'), ('La Ceiba', 'La Ceiba'), ('Aseguradora Generali', 'La Ceiba')], max_length=255)),
                ('insurance', models.CharField(choices=[('G&T', 'G&T'), ('El Roble', 'El Roble'), ('La Ceiba', 'La Ceiba'), ('Aseguradora Generali', 'La Ceiba')], max_length=255)),
                ('date', models.DateField(auto_now_add=True)),
                ('total', models.FloatField()),
            ],
        ),
    ]
