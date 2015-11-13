# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0003_auto_20150907_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='tipo_cita',
            field=models.CharField(default='a', max_length=2, choices=[('a', 'Paciente'), ('b', 'Dr'), ('c', 'Extra')]),
        ),
    ]
