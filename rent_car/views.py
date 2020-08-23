from django.urls import reverse
from django.views.generic import CreateView

from rent_car.forms.rent_car_form import RentCarForm
from rent_car.models import RentCar


class RentCarView(CreateView):
    model = RentCar
    form_class = RentCarForm
    template_name = "rent_car/index.html"

    def get_success_url(self):
        return reverse("all_cars_list")

    def abc(self, index):
        return self.get_template_names()[index]
