from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView

from .models import Food
from .permissions import IsAdminUser, IsAuthenticatedOrReadOnly
from .serializers import FoodSerializer


class FoodAPIView(APIView):
    queryset = Food.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]

    serializer_class = FoodSerializer

    def post(self, request, *args, **kwargs):

        serializer: FoodSerializer = self.serializer_class(data=request.data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)

    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(self.queryset.all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class FoodDetailAPIView(APIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

    permission_classes = [IsAdminUser]

    def get(self, request, pk: int):

        self.get_object()

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


@api_view(["GET"])
def home_page(request, format=None):
    return Response(
        {
            "food": reverse("food", request=request, format=format),
        }
    )
