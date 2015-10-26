# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0002_auto_20151026_0556'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='session',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='session',
            name='modified_date',
        ),
    ]
