# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
        ('courses', '0001_initial'),
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Endroll',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Endrolls',
                'verbose_name': 'Endroll',
                'db_table': 'endroll',
            },
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
            ],
            options={
                'verbose_name_plural': 'Sessions',
                'verbose_name': 'Session',
                'db_table': 'session',
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=300)),
                ('description', models.TextField(blank=True, default='')),
                ('slug', models.SlugField()),
                ('image', models.ImageField(max_length=255, upload_to='subjects', default='')),
                ('categories', models.ManyToManyField(to='categories.Category', related_name='subjects', db_table='category_subject')),
                ('course', models.ForeignKey(to='courses.Course')),
            ],
            options={
                'verbose_name_plural': 'Subjects',
                'verbose_name': 'Subject',
                'db_table': 'subject',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
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
                'verbose_name': 'Task',
                'db_table': 'task',
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
        migrations.AddField(
            model_name='endroll',
            name='student',
            field=models.ForeignKey(to='students.Student'),
        ),
    ]
