from django.db import models

from ars.students.models import Student
from ars.subjects.models import Subject

# Create your models here.
class Review(models.Model):
    MAX_STARS = 5
    RATING_STARS = (
            (1, 'One star'),
            (2, 'Two stars'),
            (3, 'Three stars'),
            (4, 'Four stars'),
            (5, 'Five stars'),
    )

    student = models.ForeignKey(Student)
    subject = models.ForeignKey(Subject)
    rating = models.IntegerField(choices=RATING_STARS, default=4)
    content = models.TextField(blank=True, default='')
    date_create = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"
        db_table = "Review"

    def __str__(self):
        pass

