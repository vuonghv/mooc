# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0002_auto_20151027_0905'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Endroll',
            new_name='Enroll',
        ),
        migrations.AlterModelOptions(
            name='enroll',
            options={'verbose_name': 'Enroll', 'verbose_name_plural': 'Enrolls'},
        ),
        migrations.AlterModelTable(
            name='enroll',
            table='enroll',
        ),
    ]
