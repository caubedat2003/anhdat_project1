from django.urls import path
from .views import book_list, book_detail

urlpatterns = [
    path("books/", book_list, name="book_list"),  # Show all books
    path("books/<int:book_id>/", book_detail, name="book_detail"),  # Show single book
]