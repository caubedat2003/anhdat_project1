from django.urls import path
from .views import BookListCreateAPIView, BookDetailAPIView, BookSearchAPIView

urlpatterns = [
    path('books/search/', BookSearchAPIView.as_view(), name='book-search'),
    path('books/', BookListCreateAPIView.as_view(), name='book-list-create'),
    path('books/<str:book_id>/', BookDetailAPIView.as_view(), name='book-detail'),
]
