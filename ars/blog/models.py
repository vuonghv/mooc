from django.db import models
from django.conf import settings

from ars.teachers.models import Teacher
from ars.core.models import Timestampable

# Create your models here.
class Blog(Timestampable):
    WAITING = 1
    APPROVE = 2

    STATUS_CHOICES = (
        (WAITING, 'Waiting'),
        (APPROVE, 'Approve')
    )

    teacher = models.ForeignKey(Teacher)
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField()
    content = models.TextField()
    status = models.SmallIntegerField(choices=STATUS_CHOICES, default=WAITING)
    image = models.ImageField(upload_to=settings.BLOG_DIR, max_length=255, default='', blank=False)

    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"
        db_table = 'blog'

    def __str__(self):
        return self.title

