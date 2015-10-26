from django.db import models

from ars.core.models import Timestampable, Describable


class Category(Timestampable, Describable):

    def __str__(self):
        return 'Category {}'.format(self.name)
