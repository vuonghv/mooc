# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0003_auto_20151027_0922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enroll',
            name='session',
            field=models.ForeignKey(related_name='enrolls', to='subjects.Session'),
        ),
    ]
