"""copyright (c) 2020 Beeflow Ltd.

Author Rafal Przetakowski <rafal.p@beeflow.co.uk>"""
from django.urls import path

from rent_car.views import *

urlpatterns = [
    path("cars", RentCarView.as_view(), name="rent_car_cars_list")
]
