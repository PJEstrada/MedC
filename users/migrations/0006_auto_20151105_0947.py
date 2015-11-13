# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_patientuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clinicuser',
            name='role',
            field=models.CharField(max_length=100, choices=[('Doctor', 'Doctor'), ('Secretaria', 'Secretaria'), ('Cajero', 'Cajero')]),
        ),
    ]
