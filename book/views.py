import re

from django.shortcuts import get_object_or_404
from rest_framework import generics, filters, serializers
from rest_framework.response import Response

from book.models import Book, BookHistory
from book.serializer import BookSerializer, HistorySerializer, HistoryBookPostSerializer


class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ["title", "date"]
    search_fields = ["title", "author", "genre", "date", "status"]

    def get_queryset(self):
        queryset = super().get_queryset()
        ordering = self.request.query_params.get("ordering", "date")
        return queryset.order_by(ordering)

    @staticmethod
    def validate_title(value):
        if not value[0].isupper():
            raise serializers.ValidationError("Введите название с заглавной буквы!")
        if re.search(r"[^a-zA-Zа-яА-Я0-9\s]", value):
            raise serializers.ValidationError("Введите корректное название книги!")
        return value


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class HistoryList(generics.ListCreateAPIView):
    queryset = None

    def get_serializer_class(self):
        if self.request.method == "GET":
            return HistorySerializer
        return HistoryBookPostSerializer

    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer_class()

        pk = self.kwargs.get('pk', 0)
        book = get_object_or_404(Book, pk=pk)

        book_history = BookHistory.objects.filter(booked_book=book).order_by('-changed_at')
        validated_data = serializer(instance=book_history, many=True)

        return Response(data=validated_data.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer_class()

        pk = self.kwargs.get('pk', 0)
        book = get_object_or_404(Book, pk=pk)

        pre_validated_data = serializer(data=request.data)
        pre_validated_data.is_valid(raise_exception=True)

        validated_data = pre_validated_data.validated_data

        bh = BookHistory.objects.create(booked_book=book, **validated_data)

        validated_data = HistorySerializer(instance=bh)

        return Response(data=validated_data.data)
