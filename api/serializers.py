from rest_framework import serializers

from .models import Food, FoodType, Order


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = "__all__"


class FoodTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodType
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    total_price = serializers.SerializerMethodField()
    price = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = "__all__"

    def get_total_price(self, obj):
        return obj.food.price * obj.count

    def get_price(self, obj):
        return obj.food.price
