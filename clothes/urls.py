from django.urls import path
from .views import ClothesListCreateAPIView, ClothesDetailAPIView, ClothesSearchAPIView

urlpatterns = [
    path('api/clothes/search/', ClothesSearchAPIView.as_view(), name='clothes-search'),
    path('api/clothes/', ClothesListCreateAPIView.as_view(), name='clothes-list-create'),
    path('api/clothes/<str:clothes_id>/', ClothesDetailAPIView.as_view(), name='clothes-detail'),
]