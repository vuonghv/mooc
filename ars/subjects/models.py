from django.db import models
from django.conf import settings

from ars.categories.models import Category
from ars.courses.models import Course
from ars.students.models import Student
from ars.core.models import Describable, Timestampable


class Subject(Describable, Timestampable):
    course = models.ForeignKey(Course)
    categories = models.ManyToManyField(Category, db_table="category_subject", related_name='subjects')
    slug = models.SlugField()
    image = models.ImageField(upload_to=settings.SUBJECT_DIR, max_length=255, default='', blank=False)

    class Meta:
        verbose_name = "Subject"
        verbose_name_plural = "Subjects"
        db_table = 'subject'

    def get_image_url(self):
        if self.image:
            return self.image.url
        return ''

    def __str__(self):
        return self.name

class Session(models.Model):
    subject = models.ForeignKey(Subject)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    class Meta:
        verbose_name = "Session"
        verbose_name_plural = "Sessions"
        db_table = 'session'

    def __str__(self):
        return 'Session of subject {}, starting on {}'.format(
                                self.subject.name, self.start_date)
    
class Task(Describable):
    session = models.ForeignKey(Session)
    slug = models.SlugField()
    content = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"
        db_table = 'task'

    def __str__(self):
        return 'Task {}'.format(self.name)

class Endroll(Timestampable):
    session = models.ForeignKey(Session)
    student = models.ForeignKey(Student)

    class Meta:
        verbose_name = "Endroll"
        verbose_name_plural = "Endrolls"
        db_table = 'endroll'

    def __str__(self):
        return 'Student {} enrolled subject {}, start on {}'.format(
                                self.profile.user.username,
                                self.session.subject.name,
                                self.session.start_date)
