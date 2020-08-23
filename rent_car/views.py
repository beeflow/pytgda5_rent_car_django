from django.views.generic import CreateView

from rent_car.forms.rent_car_form import RentCarForm
from rent_car.models import RentCar


class RentCarView(CreateView):
    model = RentCar
    form_class = RentCarForm
    template_name = "rent_car/index.html"
