from django.urls import path
from .views import ShoesListCreateAPIView, ShoesDetailAPIView, ShoesSearchAPIView, shoes_detail_view

urlpatterns = [
    path('api/shoes/search/', ShoesSearchAPIView.as_view(), name='shoes-search'),
    path('api/shoes/', ShoesListCreateAPIView.as_view(), name='shoes-list-create'),
    path('api/shoes/<str:shoes_id>/', ShoesDetailAPIView.as_view(), name='shoes-detail'),
    path('shoes/details/', shoes_detail_view, name='shoes-detail-view'),
]