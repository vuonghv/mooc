from django.db import models
from django.conf import settings

from ars.core.models import UserProfile


class Teacher(models.Model):
    profile = models.OneToOneField(UserProfile,
                                default=None, related_name='teacher')

    class Meta:
        db_table = 'teacher'

    def __str__(self):
        return 'Teacher {}'.format(self.name)
