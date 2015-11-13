# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='my_field2',
        ),
        migrations.AlterField(
            model_name='invoice',
            name='items',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Consulta', 'Consulta'), ('Inyeccion', 'Inyeccion'), ('La Ceiba', 'La Ceiba'), ('Aseguradora Generali', 'La Ceiba')], max_length=255),
        ),
    ]
