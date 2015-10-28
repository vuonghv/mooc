# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='content',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='review',
            name='student',
            field=models.ForeignKey(to='students.Student', related_name='reviews'),
        ),
        migrations.AlterField(
            model_name='review',
            name='subject',
            field=models.ForeignKey(to='subjects.Subject', related_name='reviews'),
        ),
    ]
