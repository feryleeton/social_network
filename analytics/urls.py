from django.urls import path
from analytics import views

urlpatterns = [
    path('', views.LikeActivityAnalytics.as_view()),
    path('user/<int:pk>', views.UserActivityAnalytics.as_view()),
]