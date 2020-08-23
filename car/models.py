from django.core.validators import MinLengthValidator
from django.db import models


class CarBrand(models.Model):
    name = models.CharField(max_length=25, null=False, blank=False, unique=True, validators=[MinLengthValidator])

    def __str__(self):
        return self.name


class CarModel(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    car_brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE, related_name="models")

    def __str__(self):
        return f"{self.car_brand} {self.name}"


class CarStatus(models.Model):
    name = models.CharField(max_length=25, null=False, blank=False, unique=True)
    uuid = models.UUIDField(null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Car Status"
        verbose_name_plural = "Car statuses"


class Car(models.Model):
    brand = models.ForeignKey(CarBrand, null=False, blank=False, on_delete=models.PROTECT, related_name="cars")
    model = models.ForeignKey(CarModel, null=False, blank=False, on_delete=models.PROTECT, related_name="cars")
    register_number = models.CharField(max_length=10, null=False, blank=False, unique=True)
    production_year = models.IntegerField(null=True, blank=True)
    status = models.ForeignKey(CarStatus, on_delete=models.PROTECT, null=True, related_name="cars")

    def __str__(self):
        return f"{self.model} - {self.register_number}"
