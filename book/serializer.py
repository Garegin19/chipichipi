import re
from rest_framework import serializers
from book.models import Book, BookHistory


class BookSerializer(serializers.ModelSerializer):

    def validate_title(self, value):
        if not value[0].isupper():
            raise serializers.ValidationError("Введите название с заглавной буквы!")
        if re.search(r"[^a-zA-Zа-яА-Я0-9\s]", value):
            raise serializers.ValidationError("Введите корректное название книги!")
        return value

    def create(self, validated_data):
        validated_data["title"] += "."
        book = Book.objects.create(**validated_data)
        return book

    def update(self, instance, validated_data):
        # status = validated_data.get('status')
        # instance = super().update(instance, validated_data)
        # if status == 'Read':
        #     BookHistory.objects.create(book=instance)
        # return instance
        pre_status = instance.status
        instance.status = super().update(instance, validated_data)
        status = validated_data.get("status")
        if status != pre_status:
            BookHistory.objects.create(book=instance)
        return instance

    class Meta:
        model = Book
        fields = ["id", "title", "author", "genre", "date", "status"]

class HistorySerializer(serializers.ModelSerializer):
#     status = serializers.CharField(source='formatted_status')
    book = BookSerializer
    class Meta:
        model = BookHistory
        fields = ["id", "book", "changed_at"]

