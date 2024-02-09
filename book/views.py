from rest_framework import generics, filters
from book.models import Book
from book.serializer import BookSerilizer, OrderingSerializer


class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerilizer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['title', 'date']
    search_fields = ['title', 'author', 'genre', 'date']

    def get_queryset(self):
        queryset = super().get_queryset()
        ordering = self.request.query_params.get('ordering', 'date')
        serialized_data = OrderingSerializer(data=self.request.query_params)
        serialized_data.is_valid(raise_exception=True)
        validated_data = serialized_data.validated_data
        return queryset.order_by(ordering)


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerilizer

