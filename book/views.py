from rest_framework import generics, filters, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
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

    def get_queryset(self):
        serializer = self.get_serializer_class()
        pk = self.kwargs.get('pk', 0)
        book_history = get_object_or_404(Book, pk=self.kwargs['pk'])
        validated_data = serializer(instance=book_history, many=True)
        return BookHistory.objects.filter(status='status').order_by('-changed_at')


    # def get(self, request, *args, **kwargs):
    #     serializer = self.get_serializer_class()
    #
    #     pk = self.kwargs.get('pk', 0)
    #     book = get_object_or_404(Book, pk=pk)
    #
    #     book_history = BookHistory.objects.filter(status='status').order_by('-changed_at')
    #     validated_data = serializer(instance=book_history, many=True)
    #
    #     return Response(data=validated_data.data)



