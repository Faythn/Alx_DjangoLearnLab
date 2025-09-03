from django.db import models

class Author(models.Model):
    """
    Author model:
    Represents an author who can write multiple books.
    Fields:
    - name: stores the author's full name.
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Book model:
    Represents a book written by an author.
    Fields:
    - title: stores the book title.
    - publication_year: stores the year of publication.
    - author: ForeignKey to Author, representing a one-to-many relationship
      (one author can have many books).
    """
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name="books", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} ({self.publication_year})"


