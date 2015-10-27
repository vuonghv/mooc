from django.db import models
from django.conf import settings

from ars.core.models import UserProfile


class Student(models.Model):
    profile = models.OneToOneField(UserProfile,
                            default=None, related_name='student')

    class Meta:
        db_table = 'student'

    def __str__(self):
        return 'Student {}'.format(self.name)
