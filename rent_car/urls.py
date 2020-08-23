"""copyright (c) 2020 Beeflow Ltd.

Author Rafal Przetakowski <rafal.p@beeflow.co.uk>"""
from django.urls import path

from rent_car.views import *

urlpatterns = [
    path("car", RentCarView.as_view(), name="rent_car")
]
