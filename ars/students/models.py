from django.db import models

from ars.core.models import AbstractAccount


class Student(AbstractAccount):

    def is_teacher(self):
        return False
