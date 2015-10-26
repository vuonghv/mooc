# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField()),
                ('description', models.TextField()),
                ('content', models.TextField()),
                ('status', models.SmallIntegerField(choices=[(1, 'Waiting'), (2, 'Approve')], default=1)),
                ('image', models.ImageField(max_length=255, default='', upload_to='blog')),
                ('teacher', models.ForeignKey(to='teachers.Teacher')),
            ],
            options={
                'db_table': 'Blog',
                'verbose_name_plural': 'Blogs',
                'verbose_name': 'Blog',
            },
        ),
    ]
