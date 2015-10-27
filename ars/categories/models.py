from django.db import models

from ars.core.models import Timestampable, Describable


class Category(Timestampable, Describable):

    class Meta:
        db_table = 'category'

    def __str__(self):
        return self.name
