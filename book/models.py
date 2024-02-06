from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=64, null=True, blank=True)
    author = models.CharField(max_length=128, null=True, blank=True)
    genre = models.CharField(max_length=64, null=True, blank=True)

    def __str__(self):
        return self.title