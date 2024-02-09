from django.db import models

from .uppercase import uppercase


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=64, unique=True, validators=[uppercase])
    author = models.CharField(max_length=128)
    genre = models.CharField(max_length=64, default="Незнакомый жанр.")
    date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.title.endswith('.'):
            self.title += '.'
        super().save(*args, **kwargs)
