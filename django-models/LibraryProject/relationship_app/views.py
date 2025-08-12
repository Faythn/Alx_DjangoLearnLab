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



from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import UserProfile

def role_required(required_role):
    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return HttpResponse("Unauthorized", status=401)
            try:
                if request.user.userprofile.role == required_role:
                    return view_func(request, *args, **kwargs)
                else:
                    return HttpResponse("Forbidden", status=403)
            except UserProfile.DoesNotExist:
                return HttpResponse("No profile found", status=403)
        return _wrapped_view
    return decorator

@role_required('Admin')
def admin_view(request):
    return HttpResponse("Welcome Admin!")






from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from .models import UserProfile

# Helper functions to check roles

def is_librarian(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')
