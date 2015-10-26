from django.db import models
from django.conf import settings

from ars.core.models import AbstractAccount


class Teacher(AbstractAccount):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='teacher')

    def is_teacher(self):
        return True

    class Meta:
        db_table = 'teacher'