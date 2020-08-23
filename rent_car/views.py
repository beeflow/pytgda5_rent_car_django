from django.views.generic import ListView

from rent_car.models import RentCar


class RentCarView(ListView):
    template_name = "rent_car/index.html"
    model = RentCar
