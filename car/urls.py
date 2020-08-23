"""copyright (c) 2020 Beeflow Ltd.

Author Rafal Przetakowski <rafal.p@beeflow.co.uk>"""
from django.urls import path

from car.views import *

urlpatterns = [
    path("", CarsListView.as_view(), name="all_cars_list")
]
