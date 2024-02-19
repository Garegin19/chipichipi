from django.contrib import admin

from book.models import Book, BookHistory

# Register your models here.
admin.site.register(Book)
admin.site.register(BookHistory)
