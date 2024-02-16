from django.db import models






class Book(models.Model):
    title = models.CharField(max_length=64, unique=True, null=True, blank=True, db_index=True)
    author = models.CharField(max_length=128, null=True, blank=True)
    genre = models.CharField(max_length=64, null=True, blank=True, default="Жанр")
    date = models.DateTimeField(auto_now_add=True, null=True, db_index=True)

    def __str__(self):
        return self.title


class BookHistory(models.Model):
    class StatusChoices(models.TextChoices):
        NOT_READ = ('Not read', 'NR')
        READ = ('Read', 'R')
        PENDING = ('Pending', 'P')
    status = models.CharField(max_length=16, choices=StatusChoices.choices, default=StatusChoices.NOT_READ)
    changed_at = models.DateTimeField(auto_now=True)
    booked_book = models.ForeignKey(to=Book, on_delete=models.CASCADE, null=True)
