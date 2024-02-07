from rest_framework import generics, request
from rest_framework.response import Response
from book.models import Book
from book.serializer import BookSerilizer, GetDateSerializer

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




