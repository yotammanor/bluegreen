from django.db import models
from core.managers import ChapterManager
from core.blue_green_utils import is_migration_applied


class Book(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name


class Chapter(models.Model):
    book = models.ForeignKey('Book',
                             on_delete=models.CASCADE,
                             related_name='chapters')
    number = models.PositiveSmallIntegerField(null=True)
    name = models.CharField(max_length=200)

    objects = ChapterManager()

    def __str__(self):
        return f'{self.book}, Chapter {self.temp_number}: {self.name}'

    @property
    def temp_number(self):
        if is_migration_applied():
            return None
        return self.number

    @temp_number.setter
    def temp_number(self, value):
        if is_migration_applied():
            return
        self.number = value
