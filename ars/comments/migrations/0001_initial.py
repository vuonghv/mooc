# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blog_teacher'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField()),
                ('blog', models.ForeignKey(to='blog.Blog')),
                ('profile', models.ForeignKey(to='core.UserProfile')),
            ],
            options={
                'verbose_name': 'Comment',
                'db_table': 'comment',
                'verbose_name_plural': 'Comments',
            },
        ),
    ]
