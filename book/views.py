from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from rest_framework.response import Response
from book.models import Book
from book.serializer import BookSerilizer

class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerilizer
    http_method_names = ['get', 'post']

class BookDetail(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerilizer
    http_method_names = ['get', 'put']