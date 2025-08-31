

# Create your models here.
from django.db import models

class Author(models.Model):
    """
    Author model stores information about book authors.
    Each Author can be linked to many Book instances (One-to-Many relationship).
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Book model stores information about books.
    Each Book is linked to one Author via a ForeignKey.
    """
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} ({self.publication_year})"
