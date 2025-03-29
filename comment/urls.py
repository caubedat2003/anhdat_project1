from django.urls import path
from .views import CommentListAPIView, AddCommentAPIView

urlpatterns = [
    path('api/comments/add/', AddCommentAPIView.as_view(), name='add_comment'),
    path('api/comments/<str:product_id>/', CommentListAPIView.as_view(), name='get_comments'),
    
]
