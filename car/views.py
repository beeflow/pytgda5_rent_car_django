from django.views.generic import ListView

from car.models import Car


class CarsListView(ListView):
    template_name = "car/index.html"
    model = Car
