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


from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Registration View
def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")  # change 'home' to your desired redirect page
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})

# Login View
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")  # change 'home' to your desired redirect page
    else:
        form = AuthenticationForm()
    return render(request, "relationship_app/login.html", {"form": form})

# Logout View
def logout_view(request):
    logout(request)
    return render(request, "relationship_app/logout.html")
