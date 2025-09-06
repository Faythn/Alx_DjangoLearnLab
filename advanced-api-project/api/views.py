# api/views.py
from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer


# List all books OR create a new one
class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Permissions: anyone can read, only authenticated can create
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# Retrieve, update, or delete a single book
class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Permissions: anyone can read, only authenticated can update/delete
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

