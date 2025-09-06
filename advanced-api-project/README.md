# Advanced API Project

This Django REST Framework project demonstrates the use of **generic views** to handle CRUD operations for a `Book` model with an `Author` relationship.

---

## 📌 Endpoints

### Book Endpoints

- **List all books**
  - `GET /api/books/`
  - Public access

- **Create a new book**
  - `POST /api/books/`
  - Requires authentication

- **Retrieve a book**
  - `GET /api/books/<id>/`
  - Public access

- **Update a book**
  - `PUT /api/books/<id>/`
  - Requires authentication

- **Delete a book**
  - `DELETE /api/books/<id>/`
  - Requires authentication

---

## 🔒 Permissions

- **Unauthenticated users** → can only view (`GET`) books.
- **Authenticated users** → can create, update, and delete books.

---

## 🛠️ Tech Stack

- Python 3.x
- Django 5.x
- Django REST Framework
- SQLite (default database)

---

## 🚀 How to Run Locally

```bash
git clone https://github.com/<your-username>/Alx_DjangoLearnLab.git
cd Alx_DjangoLearnLab/advanced-api-project

# Apply migrations
python manage.py migrate

# Run server
python manage.py runserver
