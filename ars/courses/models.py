from django.db import models

from ars.core.models import Timestampable, Describable


class TeacherCourse(models.Model):
    teacher = models.ForeignKey('ars.teachers.Teacher')
    course = models.ForeignKey('ars.courses.Course')
    is_creator = models.BooleanField(default=False)


class Course(Timestampable, Describable):
    teachers = models.ManyToManyField('ars.teachers.Teacher',
                                        through=TeacherCourse,
                                        related_name='courses')
