from django.db import models

from ars.categories.models import Category
from ars.courses.models import Course
from ars.students.models import Student
from ars.core.models import Describable, Timestampable


class Subject(Describable):
    course = models.ForeignKey(Course)
    categories = models.ManyToManyField(Category, db_table="category_subject", related_name='subjects')
    slug = models.SlugField()
    date_create = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Subject"
        verbose_name_plural = "Subjects"
        db_table = 'Subject'

    def __str__(self):
        return self.name

class Session(models.Model):
    subject = models.ForeignKey(Subject)
    date_create = models.DateTimeField(auto_now_add=True)
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()

    class Meta:
        verbose_name = "Session"
        verbose_name_plural = "Sessions"
        db_table = 'Session'

    def __str__(self):
        return 'Session of subject {}, starting on {}'.format(
                                self.subject.name, self.date_start)
    
class Task(Describable):
    session = models.ForeignKey(Session)
    slug = models.SlugField()
    content = models.TextField()
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()

    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"
        db_table = 'Task'

    def __str__(self):
        return 'Task {}'.format(self.name)

class Endroll(models.Model):
    session = models.ForeignKey(Session)
    student = models.ForeignKey(Student)
    date_create = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Endroll"
        verbose_name_plural = "Endrolls"
        db_table = 'Endroll'

    def __str__(self):
        return 'Student {} enrolled subject {}, start on {}'.format(
                                self.student.user.username,
                                self.session.subject.name,
                                self.session.date_start)
