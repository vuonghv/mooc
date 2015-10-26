from django.db import models
from django.conf import settings

from ars.core.models import AbstractAccount


class Student(AbstractAccount):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='student')

    def is_teacher(self):
        return False

    class Meta:
        db_table = 'student'
