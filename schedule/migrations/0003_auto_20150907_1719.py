# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0002_event_tipo_cita'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='tipo_cita',
            field=models.CharField(default='a', max_length=2, choices=[('a', 'Cita Inicial'), ('b', 'Consecutiva'), ('c', 'Cirugia'), ('d', 'otros')]),
        ),
    ]
