from django.db import models


class BookHistory(models.Model):
    status = models.CharField(max_length=16, choices=(
        ('READ', 'R'),
        ('UNREAD', 'N'),
        ('PENDING', 'P')
    ))
    changed_at = models.DateTimeField(auto_now=True)

class Book(models.Model):
    title = models.CharField(max_length=64, unique=True, null=True, blank=True, db_index=True)
    author = models.CharField(max_length=128, null=True, blank=True)
    genre = models.CharField(max_length=64, null=True, blank=True, default="Жанр")
    date = models.DateTimeField(auto_now_add=True, null=True, db_index=True)
    status = models.ManyToManyField(to=BookHistory)

    def __str__(self):
        return self.title

