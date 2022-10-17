from django.urls import path
from feed import views

urlpatterns = [
    path('posts/', views.PostListCreateAPIView.as_view()),
    path('posts/like/<int:pk>', views.LikePostView.as_view()),
]