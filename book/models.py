from django.db import models


class BookHistory(models.Model):
    class StatusChoices(models.TextChoices):
        NOT_READ = ('Not read', 'NR')
        READ = ('Read', 'R')
        PENDING = ('Pending', 'P')

    status = models.CharField(max_length=16, choices=StatusChoices.choices, default=StatusChoices.NOT_READ)
    changed_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.status} {self.changed_at}"


class Book(models.Model):
    class OrderingChoices(models.TextChoices):
        Title = ('title', 'title')
        Author = ('author', 'author')
        Genre = ('genre', 'genre')
        Date = ('date', 'date')

    title = models.CharField(max_length=64, unique=True, db_index=True)
    author = models.CharField(max_length=128)
    genre = models.CharField(max_length=64, default="Жанр")
    date = models.DateTimeField(auto_now_add=True, null=True, db_index=True)
    statuses = models.ManyToManyField(BookHistory, null=True, blank=True)

    def __str__(self):
        return f"{self.title} {self.genre} {self.author}"
