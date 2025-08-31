
---

### 📁 4. `delete.md`

```markdown
# Delete a Book

**Python Command:**

```python
from bookshelf.models import Book
book = Book.objects.get(id=book.id)
book.delete()
print(Book.objects.all())

#Output

(<Book: Nineteen Eighty-Four by George Orwell>,)
<QuerySet []>
