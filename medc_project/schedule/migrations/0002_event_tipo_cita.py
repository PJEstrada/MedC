# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='tipo_cita',
            field=models.CharField(max_length=2, choices=[('a', 'Paciente'), ('b', 'Dr'), ('c', 'Extra')], default='a'),
            preserve_default=True,
        ),
    ]
