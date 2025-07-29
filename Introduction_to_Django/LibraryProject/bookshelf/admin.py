
# Register your models here.
from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Show these fields in the list view
    list_display = ('title', 'author', 'publication_year')

    # Add filters on the right side
    list_filter = ('publication_year', 'author')

    # Add a search bar to search by title or author
    search_fields = ('title', 'author')
