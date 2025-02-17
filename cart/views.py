from django.shortcuts import render
from django.http import JsonResponse
from .models import Cart

def get_cart_items(request):
    if request.method == 'GET':
        carts = Cart.objects.all()
        cart_list = [
            {
                "customer": cart.customer.username,
                "product": cart.product.title,
                "quantity": cart.quantity,
                "total_price": cart.total_price
            }
            for cart in carts
        ]
        return JsonResponse({"cart_items": cart_list}, safe=False)

def cart_list_page(request):
    carts = Cart.objects.all()
    return render(request, "cart_list.html", {"carts": carts})
