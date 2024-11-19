from django.urls import path

from .views import FoodAPIView, FoodDetailAPIView, FoodTypeAPIView, OrderAPIView, OrderDetailAPIView, home_page

urlpatterns = [
    path("", home_page, name="home"),
    #
    path("food/", FoodAPIView.as_view(), name="food-list"),
    path("food/<int:pk>/", FoodDetailAPIView.as_view(), name="food-detail"),
    #
    path("food-type/", FoodTypeAPIView.as_view(), name="food-type-list"),
    path("food-type/<int:pk>/", FoodTypeAPIView.as_view(), name="food-type-detail"),
    #
    path("order/", OrderAPIView.as_view(), name="order-list"),
    path("order/<int:pk>/", OrderDetailAPIView.as_view(), name="order-detail"),
]
