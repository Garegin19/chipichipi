from rest_framework import serializers
from book.models import Book
import re


class BookSerilizer(serializers.ModelSerializer):

    def validate_title(self, value):
        if not value[0].isupper():
            raise serializers.ValidationError("Введите название с заглавной буквы!")
        if re.search(r'[^a-zA-Zа-яА-Я0-9\s]', value):
            raise serializers.ValidationError("Введите корректное название книги!")
        return value

    def create(self, validated_data):
        title = validated_data['title'] + '.'
        validated_data['title'] = title
        book = Book.objects.create(**validated_data)
        return book
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'genre', 'date', 'status']

class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'genre', 'date', 'status']