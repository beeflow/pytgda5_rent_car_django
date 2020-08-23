from django.db import IntegrityError
from django.test import TestCase

from car.models import CarBrand


class CarViewTest(TestCase):
    def test_list_has_table(self):
        response = self.client.get("/car/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "nr rejestracyjny")


class CarBrandTest(TestCase):
    def test_should_create_model(self):
        """Powinien utworzyć prawidłową markę pojazdu."""
        brand_name = "Mercedes"
        car_brand = CarBrand.objects.create(name=brand_name)
        car_brand.refresh_from_db()

        self.assertEqual(brand_name, car_brand.name)
        car_brand.delete()

    def test_should_raise_unique_exception(self):
        brand_name = "Mercedes"
        with self.assertRaises(IntegrityError):
            CarBrand.objects.create(name=brand_name)
            CarBrand.objects.create(name=brand_name)

    def test_should_raise_null_exception(self):
        with self.assertRaises(IntegrityError):
            CarBrand.objects.create(name=None)

    # def test_should_raise_blank_exception(self):
    #     car_brand = CarBrand.objects.create(name="")
    #     car_brand.refresh_from_db()
    #     print(f"-{car_brand.name}-")

    # def test_should_raise_max_length_exception(self):
    #     brand_name = "Mercedesfwefwefwefwefwefwef"
    #     CarBrand.objects.create(name=brand_name)
