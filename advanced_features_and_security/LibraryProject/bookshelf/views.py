# bookshelf/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book

# View to list books (requires 'can_view' permission)
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, "bookshelf/book_list.html", {"books": books})

# View to create a book (requires 'can_create' permission)
@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    if request.method == "POST":
        title = request.POST.get("title")
        author = request.POST.get("author")
        published_date = request.POST.get("published_date")
        Book.objects.create(title=title, author=author, published_date=published_date)
        return redirect("book_list")
    return render(request, "bookshelf/create_book.html")

# View to edit a book (requires 'can_edit' permission)
@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        book.title = request.POST.get("title")
        book.author = request.POST.get("author")
        book.published_date = request.POST.get("published_date")
        book.save()
        return redirect("book_list")
    return render(request, "bookshelf/edit_book.html", {"book": book})

# View to delete a book (requires 'can_delete' permission)
@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        book.delete()
        return redirect("book_list")
    return render(request, "bookshelf/delete_book.html", {"book": book})

from django.shortcuts import render
from .forms import ExampleForm  # ✅ Import ExampleForm safely
from .models import Book

def form_example_view(request):
    if request.method == "POST":
        form = ExampleForm(request.POST)
        if form.is_valid():
            # ✅ Safe access to validated input
            name = form.cleaned_data["name"]
            message = form.cleaned_data["message"]
            return render(request, "bookshelf/form_example.html", {"form": form, "success": True})
    else:
        form = ExampleForm()
    return render(request, "bookshelf/form_example.html", {"form": form})

def book_list_view(request):
    # ✅ Safe ORM query (no raw SQL → prevents SQL injection)
    books = Book.objects.select_related("author").all()
    return render(request, "bookshelf/book_list.html", {"books": books})

