from django.urls import path
from .views import MobileListCreateAPIView, MobileDetailAPIView, MobileSearchAPIView

urlpatterns = [
    path('mobiles/search/', MobileSearchAPIView.as_view(), name='mobile-search'),
    path('mobiles/', MobileListCreateAPIView.as_view(), name='mobile-list-create'),
    path('mobiles/<str:mobile_id>/', MobileDetailAPIView.as_view(), name='mobile-detail'),
]