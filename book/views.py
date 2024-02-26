from django.http import Http404
from rest_framework import generics, filters
from rest_framework.generics import get_object_or_404

from book.models import Book, BookHistory
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
    queryset = BookHistory.objects.all()
    serializer_class = HistorySerializer

    def get_book(self) -> Book:
        if not self.kwargs.get('pk'):
            raise Http404

        book = get_object_or_404(Book, pk=self.kwargs['pk'])
        return book

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        return BookHistory.objects.filter(book_id=pk).order_by('-changed_at')





