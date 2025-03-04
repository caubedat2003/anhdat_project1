from django.urls import path
from .views import ClothesListCreateAPIView, ClothesDetailAPIView, ClothesSearchAPIView

urlpatterns = [
    path('clothes/search/', ClothesSearchAPIView.as_view(), name='clothes-search'),
    path('clothes/', ClothesListCreateAPIView.as_view(), name='clothes-list-create'),
    path('clothes/<str:clothes_id>/', ClothesDetailAPIView.as_view(), name='clothes-detail'),
]