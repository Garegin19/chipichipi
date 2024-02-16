from rest_framework import serializers
from book.models import Book, BookHistory, StatusChoices
import re


class StatusChoicesField(serializers.ChoiceField):
    def to_internal_value(self, data):
        if isinstance(data, str):
            return dict(StatusChoices.choices)[data]
        return super().to_internal_value(data)


class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BookHistory
        fields = ["id", "status", "changed_at"]


class BookSerilizer(serializers.ModelSerializer):
    status = HistorySerializer(many=True)
    status = StatusChoicesField(choices=StatusChoices.choices)
    def validate_title(self, value):
        if not value[0].isupper():
            raise serializers.ValidationError("Введите название с заглавной буквы!")
        if re.search(r"[^a-zA-Zа-яА-Я0-9\s]", value):
            raise serializers.ValidationError("Введите корректное название книги!")
        return value

    def create(self, validated_data):
        title = validated_data["title"] + "."
        validated_data["title"] = title
        book = Book.objects.create(**validated_data)
        return book

    class Meta:
        model = Book
        fields = ["id", "title", "author", "genre", "date", "status"]
