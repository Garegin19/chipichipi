from rest_framework import generics, filters, viewsets
from rest_framework.response import Response
from book.models import Book
from book.serializer import BookSerializer, HistorySerializer


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


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class HistoryList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = HistorySerializer