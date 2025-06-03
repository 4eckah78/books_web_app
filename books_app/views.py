from rest_framework import generics

from books_app.serializers import BookSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .filters import BookFilter

from .models import Book


class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = BookFilter


class PutGetDeleteOneBook(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
