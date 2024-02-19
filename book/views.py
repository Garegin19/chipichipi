from django.http import Http404
from rest_framework import generics, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from book.models import Book
from book.serializer import BookSerializer, HistorySerializer, OrderingSerializer


class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    ordering_serializer = OrderingSerializer
    http_method_names = ["get", "post"]

    def get_queryset(self):
        serializing = self.ordering_serializer(data=self.request.query_params)
        serializing.is_valid(raise_exception=True)
        validated = serializing.validated_data
        return self.queryset.order_by(validated["ordering"])


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    http_method_names = ["get", "post", "delete"]


class HistoryList(generics.ListCreateAPIView):
    serializer_class = HistorySerializer

    def get_book(self) -> Book:
        if not self.kwargs.get('pk'):
            raise Http404

        book = get_object_or_404(Book, pk=self.kwargs['pk'])
        return book

    def get_queryset(self):
        book = self.get_book()
        return book.statuses.order_by('-changed_at')

    def create(self, request, *args, **kwargs):
        book = self.get_book()
        serializing = self.serializer_class(data=request.data)
        serializing.is_valid(raise_exception=True)
        validated_data = serializing.validated_data
        book.statuses.create(**validated_data)
        return Response(status=status.HTTP_201_CREATED)
