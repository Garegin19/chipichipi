from django.db import models

class StatusChoices(models.TextChoices):
    NOT_READ = 'Not read', 'NR'
    READ = 'Read', 'R'
    PENDING = 'Pending', 'P'


class Book(models.Model):
    title = models.CharField(max_length=64, unique=True, null=True, blank=True, db_index=True)
    author = models.CharField(max_length=128, null=True, blank=True)
    genre = models.CharField(max_length=64, null=True, blank=True, default="Жанр")
    date = models.DateTimeField(auto_now_add=True, null=True, db_index=True)
    status = models.CharField(max_length=16, null=True, blank=True, choices=StatusChoices, default=StatusChoices.NOT_READ)

    def __str__(self):
        return self.title

    @property
    def formatted_status(self):
        if self.status:
            return dict(self.status._meta.get_field('status').choices).get(self.status)
        return None

class BookHistory(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    status = models.CharField(max_length=16, null=True, blank=True, choices=StatusChoices)
    changed_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.status = self.book.status
        super().save(*args, **kwargs)

