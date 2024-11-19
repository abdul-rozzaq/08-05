from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView

from .models import Food, FoodType, Order
from .permissions import IsAdminUser, IsAuthenticatedOrReadOnly
from .serializers import FoodSerializer, FoodTypeSerializer, OrderSerializer


class ListCreateAPIView(APIView):
    queryset = None
    serializer_class = None
    permission_classes = [IsAuthenticatedOrReadOnly]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)

    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(self.queryset.all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class DetailAPIView(APIView):
    queryset = None
    serializer_class = None
    permission_classes = [IsAdminUser]

    def get(self, request, pk: int):
        obj = self.get_object()
        serializer = self.serializer_class(instance=obj)

        return Response(serializer.data)

    def put(self, request, pk: int):
        obj = self.get_object()
        serializer = self.serializer_class(instance=obj, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

    def delete(self, request, pk: int):
        obj = self.get_object()
        obj.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_object(self):
        return get_object_or_404(self.queryset.all(), **self.kwargs)


class FoodTypeAPIView(ListCreateAPIView):
    queryset = FoodType.objects.all()
    serializer_class = FoodTypeSerializer


class FoodTypeDetailAPIView(DetailAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer


class FoodAPIView(ListCreateAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer


class FoodDetailAPIView(DetailAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer


class OrderAPIView(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderDetailAPIView(DetailAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


@api_view(["GET"])
def home_page(request, format=None):
    return Response(
        {
            "food": reverse("food", request=request, format=format),
        }
    )
