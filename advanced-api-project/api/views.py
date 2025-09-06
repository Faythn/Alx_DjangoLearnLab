from rest_framework import generics, permissions, filters
from django_filters import rest_framework as drf_filters
from .models import Book
from .serializers import BookSerializer

# Book list view with filtering, searching, ordering
class ListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]  # ✅ USES IsAuthenticatedOrReadOnly

    filter_backends = [drf_filters.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title', 'author', 'publication_year']
    search_fields = ['title', 'author__name']   # ✅ search by related author name
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']


# Book create view
class CreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # ✅ USES IsAuthenticated


# Book update view
class UpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


# Book delete view
class DeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

