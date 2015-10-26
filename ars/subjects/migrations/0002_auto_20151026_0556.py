# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='endroll',
            table='endroll',
        ),
        migrations.AlterModelTable(
            name='session',
            table='session',
        ),
        migrations.AlterModelTable(
            name='subject',
            table='subject',
        ),
        migrations.AlterModelTable(
            name='task',
            table='task',
        ),
    ]
