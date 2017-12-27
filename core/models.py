from django.db import models


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

    def __str__(self):
        return f'{self.book}, Chapter {self.number}: {self.name}'
