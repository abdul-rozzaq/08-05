from django.urls import path

from .views import FoodAPIView, FoodDetailAPIView, home_page

urlpatterns = [
    path("", home_page, name="home"),
    path("food/", FoodAPIView.as_view(), name="food"),
    path("food/<int:pk>/", FoodDetailAPIView.as_view(), name="food-detail"),
]
