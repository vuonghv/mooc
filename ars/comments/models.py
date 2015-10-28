from django.db import models

from ars.blog.models import Blog
from ars.core.models import UserProfile

# Create your models here.

class Comment(models.Model):
    create_date = models.DateTimeField(auto_now_add=True)
    profile = models.ForeignKey(UserProfile)
    blog = models.ForeignKey(Blog)
    content = models.TextField()

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
        db_table = 'comment'

    def __str__(self):
        return self.content

