from django.urls import path
from .views import BookListCreateAPIView, BookDetailAPIView, BookSearchAPIView, book_detail_view

urlpatterns = [
    path('api/books/search/', BookSearchAPIView.as_view(), name='book-search'),
    path('api/books/', BookListCreateAPIView.as_view(), name='book-list-create'),
    path('api/books/<str:book_id>/', BookDetailAPIView.as_view(), name='book-detail'),
    path('books/details/', book_detail_view, name='book-detail-view'),
]
