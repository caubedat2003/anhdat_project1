from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Book, Category

# View to display all books
def book_list(request):
    books = Book.objects.all()
    return render(request, "book_list.html", {"books": books})

# View to display a single book by ID
def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, "book_detail.html", {"book": book})

