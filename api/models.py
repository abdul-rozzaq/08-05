from django.core.validators import MinValueValidator
from django.db import models


class FoodType(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self) -> str:
        return self.name


class Food(models.Model):
    name = models.CharField(max_length=128)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self) -> str:
        return self.name


class Order(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    count = models.IntegerField(validators=[MinValueValidator(1)], default=1)

    def __str__(self) -> str:
        return super().__str__()
