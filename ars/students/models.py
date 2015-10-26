from django.db import models
from django.conf import settings

from ars.core.models import AbstractAccount


class Student(AbstractAccount):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='student')

    def is_teacher(self):
        return False

    def __str__(self):
        return 'Student {}'.format(self.name)
