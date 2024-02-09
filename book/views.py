from rest_framework import generics, filters
from book.models import Book
from book.serializer import BookSerilizer


class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerilizer


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerilizer

class GetDate(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerilizer

class GetDateForBook(generics.RetrieveUpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerilizer

class SearchBook(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerilizer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']

# class OrderDate(generics.ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = GetDateSerializer
#     filter_backends = [filters.OrderingFilter]
#     ordering_fields = ['date']

class OrderDate(generics.ListAPIView):
    queryset = Book.objects.all().order_by('-date')
    serializer_class = BookSerilizer
    ordering_fields = ['date']

# class GetBookDate(generics.ListAPIView):
#     queryset = Book.objects.all().order_by('-date')
#     serializer_class = BookSerilizer
#     def get_queryset(self):
#         queryset = super().get_queryset()
#         date_filter = self.request.GET.get('date')
#         if date_filter:
#             queryset = queryset.filter(date_filter='date')
#         return queryset

class SearchDate(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerilizer
    filter_backends = [filters.SearchFilter]
    search_fields = ['date']
    def get_queryset(self):
        queryset = Book.objects.all().order_by('-date', 'title')
        date_filter = self.request.GET.get('date')
        if date_filter:
            queryset = queryset.filter(date_filter='date')
        return queryset

