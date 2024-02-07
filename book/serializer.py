from rest_framework import serializers
from book.models import Book


class BookSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class GetDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['date']

class TitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title']



