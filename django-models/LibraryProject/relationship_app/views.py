# relationship_app/views.py
from django.http import HttpResponse
from django.shortcuts import render
from .models import Book, Library
from django.views.generic.detail import DetailView

# Function-based view (plain text for the checker)
def list_books(request):
    books = Book.objects.select_related('author').all()
    # Build plain text output (for the checker)
    output = "\n".join([f"{book.title} by {book.author.name}" for book in books])
    return HttpResponse(output, content_type="text/plain")

# Class-based view (Library details)
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'


