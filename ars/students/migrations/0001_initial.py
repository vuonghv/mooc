# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('profile', models.OneToOneField(default=None, related_name='student', to='core.UserProfile')),
            ],
            options={
                'db_table': 'student',
            },
        ),
    ]
