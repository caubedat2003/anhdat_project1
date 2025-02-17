from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Book, Category

# View to display all books
def book_list(request):
    books = Book.objects.all()
    return render(request, "book_list.html", {"books": books})
    # data = {"books": list(books.values("id", "title", "author", "price", "category", "created_at"))}
    # return JsonResponse(data)

# View to display a single book by ID
def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, "book_detail.html", {"book": book})
    # data = {
    #     "id": book.id,
    #     "title": book.title,
    #     "author": book.author,
    #     "category": book.Category.name if book.category else None,
    #     "price": book.price,
    #     "created_at": book.created_at,
    # }
    # return JsonResponse(data)

