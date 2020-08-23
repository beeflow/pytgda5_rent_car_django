"""copyright (c) 2020 Beeflow Ltd.

Author Rafal Przetakowski <rafal.p@beeflow.co.uk>"""
from uuid import UUID

from django import forms
from django.conf import settings

from car.models import Car, CarStatus
from customer.models import Customer
from rent_car.forms.horizontalformhelper import HorizontalFormHelper
from rent_car.models import RentCar


class RentCarForm(forms.ModelForm):
    car = forms.ModelChoiceField(
        queryset=Car.objects.exclude(
            status=CarStatus.objects.get(
                uuid=UUID(settings.CAR_STATUS_RENT)
            )
        )
    )

    class Meta:
        model = RentCar
        fields = ("car", "customer")

    def __init__(self, *args, **kwargs):
        self.helper = HorizontalFormHelper()
        super(RentCarForm, self).__init__(*args, **kwargs)

        self.helper.add_submit("Wypożycz")

    def save(self, commit=True):
        car: Car = self.cleaned_data.get("car")
        customer: Customer = self.cleaned_data.get("customer")

        return RentCar.objects.create(car=car, customer=customer)
