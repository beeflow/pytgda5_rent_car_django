"""copyright (c) 2020 Beeflow Ltd.

Author Rafal Przetakowski <rafal.p@beeflow.co.uk>"""
from django.forms import ModelForm

from rent_car.forms.horizontalformhelper import HorizontalFormHelper
from rent_car.models import RentCar


class RentCarForm(ModelForm):
    class Meta:
        model = RentCar
        fields = ("car", "customer")

    def __init__(self, *args, **kwargs):
        self.helper = HorizontalFormHelper()
        super(RentCarForm, self).__init__(*args, **kwargs)

        self.helper.add_submit("Wypożycz")
