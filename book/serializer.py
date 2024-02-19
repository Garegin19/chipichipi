import re

from rest_framework import serializers

from book.models import Book, BookHistory


class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BookHistory
        fields = "__all__"


class BookSerializer(serializers.ModelSerializer):

    @staticmethod
    def validate_title(value):
        if not value[0].isupper():
            raise serializers.ValidationError("Введите название с заглавной буквы!")
        if re.search(r"[^a-zA-Zа-яА-Я0-9\s]", value):
            raise serializers.ValidationError("Введите корректное название книги!")
        return value

    class Meta:
        model = Book
        exclude = ("statuses",)


class OrderingSerializer(serializers.Serializer):
    ordering = serializers.ChoiceField(choices=Book.OrderingChoices.choices, default=Book.OrderingChoices.Date)
