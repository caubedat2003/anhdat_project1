from django.urls import path
from .views import register_user, register_page, login_user, login_page

urlpatterns = [
    path('register/', register_user, name='register_user'),
    path('register-page/', register_page, name='register_page'),
    path('login-page/', login_page, name='login_page'),
    path('login/', login_user, name='login_user'),
]