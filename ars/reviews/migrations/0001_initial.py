# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
        ('subjects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('rating', models.IntegerField(choices=[(1, 'One star'), (2, 'Two stars'), (3, 'Three stars'), (4, 'Four stars'), (5, 'Five stars')], default=4)),
                ('content', models.TextField(blank=True, default='')),
                ('student', models.ForeignKey(to='students.Student')),
                ('subject', models.ForeignKey(to='subjects.Subject')),
            ],
            options={
                'verbose_name_plural': 'Reviews',
                'db_table': 'review',
                'verbose_name': 'Review',
            },
        ),
    ]
