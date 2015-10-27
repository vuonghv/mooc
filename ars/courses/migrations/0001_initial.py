# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=300)),
                ('description', models.TextField(blank=True, default='')),
            ],
            options={
                'db_table': 'course',
            },
        ),
        migrations.CreateModel(
            name='TeacherCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_creator', models.BooleanField(default=False)),
                ('course', models.ForeignKey(to='courses.Course')),
                ('teacher', models.ForeignKey(to='teachers.Teacher')),
            ],
            options={
                'db_table': 'teacher_course',
            },
        ),
        migrations.AddField(
            model_name='course',
            name='teachers',
            field=models.ManyToManyField(through='courses.TeacherCourse', related_name='courses', to='teachers.Teacher'),
        ),
    ]
