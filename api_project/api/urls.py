# api/urls.py
from django.urls import path
from .views import BookList

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),  # maps to BookList view
]


# api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet

# Create a router and register our viewset
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # Route for the BookList view (ListAPIView)
    path('books/', BookList.as_view(), name='book-list'),

    # Include router URLs for BookViewSet
    path('', include(router.urls)),
]


from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import BookList

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),  # token retrieval endpoint
]
