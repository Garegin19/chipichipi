from rest_framework import serializers
from book.models import Book
import re
from django.core.exceptions import ValidationError

class BookSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'genre', 'date']

    def create(self, validated_data):
        title = validated_data['title'] + '.'
        validated_data['title'] = title
        book = Book.objects.create(**validated_data)
        return book


CHOICES = (
    ("title", "title"),
    ("author", "author"),
    ("genre", "genre"),
    ("-title", "-title"),
    ("-author", "-author"),
    ("-genre", "-genre"),
)
class OrderingSerializer(serializers.Serializer):
    ordering = serializers.ChoiceField(choices=CHOICES, default="title")





