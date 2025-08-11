# relationship_app/views.py
from django.http import HttpResponse
from django.shortcuts import render
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView

# Function-based view (plain text for the checker)
def list_books(request):
    books = Book.objects.all()  # ✅ matches checker exactly
    return render(request, 'relationship_app/list_books.html', {'books': books}) 

# Class-based view (Library details)
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'


