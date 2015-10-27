# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField()),
                ('description', models.TextField()),
                ('content', models.TextField()),
                ('status', models.SmallIntegerField(choices=[(1, 'Waiting'), (2, 'Approve')], default=1)),
                ('image', models.ImageField(upload_to='blog', default='', max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Blogs',
                'db_table': 'blog',
                'verbose_name': 'Blog',
            },
        ),
    ]
