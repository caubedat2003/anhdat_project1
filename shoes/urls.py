from django.urls import path
from .views import ShoesListCreateAPIView, ShoesDetailAPIView, ShoesSearchAPIView

urlpatterns = [
    path('shoes/search/', ShoesSearchAPIView.as_view(), name='shoes-search'),
    path('shoes/', ShoesListCreateAPIView.as_view(), name='shoes-list-create'),
    path('shoes/<str:shoes_id>/', ShoesDetailAPIView.as_view(), name='shoes-detail'),
]