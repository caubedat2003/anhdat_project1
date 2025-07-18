from django.urls import include, path
from .views import register_user, register_page, login_user, login_page, get_all_customers, customer_list_page, CustomerListCreateView, CustomerDetailView, CustomerSearchView, logout_user, CustomerAddressView, AddressViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'addresses', AddressViewSet)

urlpatterns = [
    path('register/', register_user, name='register_user'),
    path('register-page/', register_page, name='register_page'),
    path('login-page/', login_page, name='login_page'),
    path('login/', login_user, name='login_user'),
    # path('customers/', get_all_customers, name='get_all_customers'),
    path('customers-page/', customer_list_page, name='customer_list_page'),
    path('customers/', CustomerListCreateView.as_view(), name='customer-list-create'),
    path('customers/<int:pk>/', CustomerDetailView.as_view(), name='customer-detail'),
    path('customers/search/', CustomerSearchView.as_view(), name='customer-search'),
    path('customers/<int:customer_id>/address/', CustomerAddressView.as_view(), name='get-customer-address'),
    path('', include(router.urls)),
    path('logout/', logout_user, name='logout_user'),
]

