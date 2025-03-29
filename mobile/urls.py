from django.urls import path
from .views import MobileListCreateAPIView, MobileDetailAPIView, MobileSearchAPIView, mobile_detail_view

urlpatterns = [
    path('api/mobiles/search/', MobileSearchAPIView.as_view(), name='mobile-search'),
    path('api/mobiles/', MobileListCreateAPIView.as_view(), name='mobile-list-create'),
    path('api/mobiles/<str:mobile_id>/', MobileDetailAPIView.as_view(), name='mobile-detail'),
    path('mobiles/details/', mobile_detail_view, name='mobile-detail-view'),
]