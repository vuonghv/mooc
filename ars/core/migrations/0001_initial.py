# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user', models.OneToOneField(primary_key=True, to=settings.AUTH_USER_MODEL, related_name='profile', serialize=False)),
                ('avatar', models.ImageField(upload_to='avatars')),
                ('modified_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
