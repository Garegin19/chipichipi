from rest_framework import serializers

from book.models import Book, BookHistory


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"


class HistorySerializer(serializers.ModelSerializer):
    booked_book = BookSerializer(read_only=True)
    class Meta:
        model = BookHistory
        fields = "__all__"


class HistoryBookPostSerializer(serializers.Serializer):
    status = serializers.ChoiceField(choices=BookHistory.StatusChoices, default=BookHistory.StatusChoices.NOT_READ)
