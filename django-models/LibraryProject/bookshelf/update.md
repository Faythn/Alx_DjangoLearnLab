
---

### 📁 3. `update.md`

```markdown
# Update a Book Title

**Python Command:**

```python
book = Book.objects.get(id=book.id)
book.title = "Nineteen Eighty-Four"
book.save()
print(Book.objects.get(id=book.id).title)

#Output
Nineteen Eighty-Four
