from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from .models import Author, Book


class BookAPITests(APITestCase):
    """Unit tests for Book API endpoints including CRUD, filtering, search, and ordering."""

    def setUp(self):
        # Create a user for authenticated requests
        self.user = User.objects.create_user(username="testuser", password="password123")
        self.client = APIClient()

        # Create sample author and book
        self.author = Author.objects.create(name="Faith Kioko")
        self.book = Book.objects.create(
            title="My First API",
            publication_year=2024,
            author=self.author
        )

        # Define endpoints
        self.list_url = reverse("book-list")
        self.detail_url = reverse("book-detail", args=[self.book.id])

    def test_list_books(self):
        """Test retrieving the list of books (GET /books/)."""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("My First API", str(response.data))

    def test_retrieve_book(self):
        """Test retrieving a single book (GET /books/<id>/)."""
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "My First API")

    def test_create_book_requires_authentication(self):
        """Test that creating a book requires login."""
        data = {"title": "New Book", "publication_year": 2023, "author": self.author.id}
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)  # not logged in

        # Now authenticate
        self.client.login(username="testuser", password="password123")
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_book(self):
        """Test updating an existing book."""
        self.client.login(username="testuser", password="password123")
        data = {"title": "Updated Title", "publication_year": 2024, "author": self.author.id}
        response = self.client.put(self.detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Updated Title")

    def test_delete_book(self):
        """Test deleting a book."""
        self.client.login(username="testuser", password="password123")
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book.id).exists())

    def test_filter_books_by_title(self):
        """Test filtering books by title."""
        response = self.client.get(self.list_url, {"title": "My First API"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("My First API", str(response.data))

    def test_search_books(self):
        """Test searching books by title."""
        response = self.client.get(self.list_url, {"search": "My First"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("My First API", str(response.data))

    def test_order_books_by_publication_year(self):
        """Test ordering books by publication_year."""
        Book.objects.create(title="Older Book", publication_year=2000, author=self.author)
        response = self.client.get(self.list_url, {"ordering": "publication_year"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        years = [book["publication_year"] for book in response.data]
        self.assertEqual(years, sorted(years))
