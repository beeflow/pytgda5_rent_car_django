from uuid import UUID

from django.conf import settings
from django.db import models
from django.utils import timezone

from car.models import Car, CarStatus
from customer.models import Customer


class RentCarException(Exception):
    pass


class RentCarQuerySet(models.QuerySet):
    def create(self, **kwargs):
        car = kwargs.get("car")

        if str(car.status.uuid) != settings.CAR_STATUS_AVAILABLE:
            raise RentCarException("Samochód jest niedostępny")

        car.status = CarStatus.objects.get(uuid=UUID(settings.CAR_STATUS_RENT))
        car.save()

        return super(RentCarQuerySet, self).create(**kwargs)

    def return_car(self, car):
        # 1. Znaleźć wypożyczenie dla tego auta
        rent_car = self.get(car=car, return_time=None)

        # 2. Wtawić datę zwrotu
        rent_car.return_time = timezone.now()
        rent_car.save()

        # 3. Zmienić status auta
        car.status = CarStatus.objects.get(uuid=UUID(settings.CAR_STATUS_AVAILABLE))
        car.save()


class RentCar(models.Model):
    car = models.ForeignKey(Car, on_delete=models.PROTECT)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    rent_time = models.DateTimeField(null=False, blank=False, default=timezone.now)
    return_time = models.DateTimeField(null=True)

    objects = RentCarQuerySet.as_manager()

    def __str__(self):
        return f"{self.car.register_number} rent by: {self.customer} " \
               f"on {self.rent_time} returned: {self.return_time if self.return_time else ''}"
