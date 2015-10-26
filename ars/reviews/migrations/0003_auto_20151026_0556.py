# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_review_subject'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='review',
            table='review',
        ),
    ]
