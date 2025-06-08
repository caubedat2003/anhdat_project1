"""
URL configuration for anhdat_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from customer.views import register_page, login_page, customer_list_page
from product.views import product_list
from django.shortcuts import render
from django.conf import settings
from django.conf.urls.static import static

def home_page(request):
    return render(request, "home.html")

def address_page(request):
    return render(request, "address.html")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/customer/', include('customer.urls')),
    path('register/', register_page, name='register_page'),
    path('login/', login_page, name='login_page'),
    path('', home_page, name="home_page"),
    path('customer_list/', customer_list_page, name="customer_list_page"),
    path("", include("book.urls")),
    path("", include("mobile.urls")),
    path("", include("clothes.urls")),
    path("", include("shoes.urls")),
    path("", include("cart.urls")),
    path("", include("order.urls")),
    path("", include("shipping.urls")),
    path("", include("paying.urls")),
    path("", include("comment.urls")),
    path("products/", product_list, name="product_list"),
    path('address/', address_page, name='address_page'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
