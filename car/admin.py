from uuid import UUID

from django.conf import settings
from django.contrib import admin

from car.models import CarStatus, Car


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):

    @staticmethod
    def is_available(obj):
        return obj.status.uuid == UUID(settings.CAR_STATUS_AVAILABLE)

    list_display = ("register_number", "brand", "model", "is_available")


@admin.register(CarStatus)
class CarStatusAdmin(admin.ModelAdmin):
    @staticmethod
    def cars(obj):
        return obj.cars.count()

    list_display = ("name", "cars")
