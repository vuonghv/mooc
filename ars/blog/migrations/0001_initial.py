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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField()),
                ('description', models.TextField()),
                ('content', models.TextField()),
                ('status', models.SmallIntegerField(choices=[(1, 'Waiting'), (2, 'Approve')], default=1)),
                ('image', models.ImageField(max_length=255, upload_to='blog', default='')),
            ],
            options={
                'verbose_name_plural': 'Blogs',
                'verbose_name': 'Blog',
                'db_table': 'blog',
            },
        ),
    ]
