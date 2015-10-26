from django.db import models
from django.conf import settings


class Timestampable(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Describable(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField(blank=True, default='')

    class Meta:
        abstract = True


class AbstractAccount(models.Model):
    avatar = models.ImageField(upload_to='avatars')
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def is_teacher(self):
        raise NotImplementedError
