# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
        ('students', '0001_initial'),
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Endroll',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'Endroll',
                'verbose_name_plural': 'Endrolls',
                'verbose_name': 'Endroll',
            },
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'Session',
                'verbose_name_plural': 'Sessions',
                'verbose_name': 'Session',
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=300)),
                ('description', models.TextField(blank=True, default='')),
                ('slug', models.SlugField()),
                ('image', models.ImageField(max_length=255, default='', upload_to='subjects')),
                ('categories', models.ManyToManyField(db_table='category_subject', to='categories.Category', related_name='subjects')),
                ('course', models.ForeignKey(to='courses.Course')),
            ],
            options={
                'db_table': 'Subject',
                'verbose_name_plural': 'Subjects',
                'verbose_name': 'Subject',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=300)),
                ('description', models.TextField(blank=True, default='')),
                ('slug', models.SlugField()),
                ('content', models.TextField()),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('session', models.ForeignKey(to='subjects.Session')),
            ],
            options={
                'db_table': 'Task',
                'verbose_name_plural': 'Tasks',
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
        migrations.AddField(
            model_name='endroll',
            name='student',
            field=models.ForeignKey(to='students.Student'),
        ),
    ]
