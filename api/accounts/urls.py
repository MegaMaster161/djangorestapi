from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import UserProfileListCreateView, userProfileDetailView

urlpatterns = [
    #Получаем все профили 
    path("all-profiles", UserProfileListCreateView.as_view(), name="all-profiles"),
    #детализируем корректного пользователя 
    path("profile/<int:pk>", userProfileDetailView.as_view(), name="profile"),
]