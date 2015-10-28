# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0006_auto_20151028_0847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='session',
            field=models.ForeignKey(related_name='tasks', to='subjects.Session'),
        ),
    ]
