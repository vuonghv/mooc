from django.db import models

from ars.core.models import Timestampable, Describable
from ars.teachers.models import Teacher


class Course(Timestampable, Describable):
    teachers = models.ManyToManyField(Teacher,
                            through='TeacherCourse', related_name='courses')

    def __str__(self):
        return 'Course {}'.format(self.name)


class TeacherCourse(models.Model):
    teacher = models.ForeignKey(Teacher)
    course = models.ForeignKey(Course)
    is_creator = models.BooleanField(default=False)
