from django.db import models
from core.managers import ChapterManager


class Book(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name


class Chapter(models.Model):
    book = models.ForeignKey('Book',
                             on_delete=models.CASCADE,
                             related_name='chapters')
    name = models.CharField(max_length=200)

    objects = ChapterManager()

    def __str__(self):
        return f'{self.book}, Chapter: {self.name}'
