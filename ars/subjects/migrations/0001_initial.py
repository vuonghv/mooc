# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
        ('core', '0001_initial'),
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Endroll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('profile', models.ForeignKey(to='core.UserProfile')),
            ],
            options={
                'verbose_name_plural': 'Endrolls',
                'db_table': 'endroll',
                'verbose_name': 'Endroll',
            },
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
            ],
            options={
                'verbose_name_plural': 'Sessions',
                'db_table': 'session',
                'verbose_name': 'Session',
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=300)),
                ('description', models.TextField(blank=True, default='')),
                ('slug', models.SlugField()),
                ('image', models.ImageField(upload_to='subjects', default='', max_length=255)),
                ('categories', models.ManyToManyField(db_table='category_subject', related_name='subjects', to='categories.Category')),
                ('course', models.ForeignKey(to='courses.Course')),
            ],
            options={
                'verbose_name_plural': 'Subjects',
                'db_table': 'subject',
                'verbose_name': 'Subject',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('description', models.TextField(blank=True, default='')),
                ('slug', models.SlugField()),
                ('content', models.TextField()),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('session', models.ForeignKey(to='subjects.Session')),
            ],
            options={
                'verbose_name_plural': 'Tasks',
                'db_table': 'task',
                'verbose_name': 'Task',
            },
        ),
        migrations.AddField(
            model_name='session',
            name='subject',
            field=models.ForeignKey(to='subjects.Subject'),
        ),
        migrations.AddField(
            model_name='endroll',
            name='session',
            field=models.ForeignKey(to='subjects.Session'),
        ),
    ]
