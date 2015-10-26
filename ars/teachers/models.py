from django.db import models

from ars.core.models import AbstractAccount


class Teacher(AbstractAccount):

    def is_teacher(self):
        return True
