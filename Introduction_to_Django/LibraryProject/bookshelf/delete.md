
---

### 📁 4. `delete.md`

```markdown
# Delete a Book

**Python Command:**

```python
book = Book.objects.get(id=book.id)
book.delete()
print(Book.objects.all())

#Output

(<Book: Nineteen Eighty-Four by George Orwell>,)
<QuerySet []>
