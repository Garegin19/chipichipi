import re
from rest_framework import serializers
from book.models import Book, BookHistory

class BookSerializer(serializers.ModelSerializer):

    def validate_title(self, value):
        if not value[0].isupper():
            raise serializers.ValidationError("Введите название с заглавной буквы!")
        if self.context['request'].method == 'POST':
            if re.search(r"[^a-zA-Zа-яА-Я0-9\s]", value):
                raise serializers.ValidationError("Введите корректное название книги!")
            return value

    def create(self, validated_data):
        validated_data["title"] += "."
        book = Book.objects.create(**validated_data)
        return book

    def update(self, instance, validated_data):
        # pre_status = instance.status
        instance.status = validated_data.get("status")
        BookHistory.objects.create(book=instance, status=instance.status)
        instance.save()
        return instance

    def to_representation(self, instance):
        res = super().to_representation(instance)
        res["date"] = instance.date.strftime("%d.%m.%Y %H:%M:%S")
        return res
    class Meta:
        model = Book
        fields = ["id", "title", "author", "genre", "date", "status"]


class HistorySerializer(serializers.ModelSerializer):
    title = serializers.CharField(source="book.title")

    def to_representation(self, instance):
        res = super().to_representation(instance)
        res["changed_at"] = instance.changed_at.strftime("%d.%m.%Y %H:%M:%S")
        return res
    class Meta:
        model = BookHistory
        fields = ["book", "title", "changed_at", "status"]
        many = True



