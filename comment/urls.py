from django.urls import path
from .views import CommentListAPIView, AddCommentAPIView, RecommendBooksAPIView

urlpatterns = [
    path('api/comments/add/', AddCommentAPIView.as_view(), name='add_comment'),
    path('api/comments/recommend_books/', RecommendBooksAPIView.as_view(), name='recommend_books'),
    path('api/comments/details/<str:product_id>/', CommentListAPIView.as_view(), name='get_comments'),
]
