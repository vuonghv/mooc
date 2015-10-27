# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='subject',
            field=models.ForeignKey(to='subjects.Subject', related_name='sessions'),
        ),
    ]
