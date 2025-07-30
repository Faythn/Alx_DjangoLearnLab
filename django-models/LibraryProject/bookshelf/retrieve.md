
---

### 📁 2. `retrieve.md`

```markdown
# Retrieve a Book

**Python Command:**

```python
from bookshelf.models import Book
retrieved_book = Book.objects.get(id=book.id)
print(retrieved_book.title)

#output
1984
