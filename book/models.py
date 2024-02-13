from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=64, unique=True, null=True, blank=True, db_index=True)
    author = models.CharField(max_length=128, null=True, blank=True)
    genre = models.CharField(max_length=64, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return self.title



