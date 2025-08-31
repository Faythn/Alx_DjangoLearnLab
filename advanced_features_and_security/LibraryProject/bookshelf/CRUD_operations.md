# Django Shell: CRUD Operations on Book Model

## 1. Create

**Command:**

```python
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(book)

#output
1984 by George Orwell

2. Retrieve
Command:
retrieved_book = Book.objects.get(id=book.id)
print(retrieved_book.title)

#Output
1984


book = Book.objects.get(id=book.id)
book.title = "Nineteen Eighty-Four"
book.save()
print(Book.objects.get(id=book.id).title)
#output
Nineteen Eighty-Four


book = Book.objects.get(id=book.id)
book.delete()
print(Book.objects.all())

#output
(<Book: Nineteen Eighty-Four by George Orwell>,)
<QuerySet []>
