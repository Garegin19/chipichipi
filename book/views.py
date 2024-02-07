from rest_framework import generics, filters
from book.models import Book
from book.serializer import BookSerilizer, GetDateSerializer, TitleSerializer

class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerilizer


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerilizer

class GetDate(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = GetDateSerializer

class GetDateForBook(generics.RetrieveUpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = GetDateSerializer

class SearchBook(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = TitleSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']

# class OrderDate(generics.ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = GetDateSerializer
#     filter_backends = [filters.OrderingFilter]
#     ordering_fields = ['date']

class OrderDate(generics.ListAPIView):
    queryset = Book.objects.all().order_by('-date')
    serializer_class = GetDateSerializer
    ordering_fields = ['date']




