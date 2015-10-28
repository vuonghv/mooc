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

    @property
    def username(self):
        return self.profile.user.username

    @property
    def first_name(self):
        return self.profile.user.first_name

    @property
    def last_name(self):
        return self.profile.user.last_name

    @property
    def full_name(self):
        return self.profile.user.get_full_name()
