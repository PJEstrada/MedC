# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0003_auto_20151101_1803'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='customer_segundo_nombre',
        ),
    ]
