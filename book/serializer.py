from rest_framework import serializers
from book.models import Book


class BookSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'genre', 'date']

# class TitleSerializer(serializers.Serializer):
#     title = serializers.CharField(validators=[uppercase])

# class GetDateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Book
#         fields = ['date']
#
# class TitleSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Book
#         fields = ['title']
#
# class DateTitleSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Book
#         fields = ['title', 'date']




