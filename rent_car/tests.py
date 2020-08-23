import mock
from django.test import TestCase

from rent_car.views import RentCarView
from unittest_data_provider import data_provider


class RentCarViewTest(TestCase):
    def setUp(self) -> None:
        self.view = RentCarView()
        self.template_names = ["abc", "def", "ghi", "jkl"]

    def tearDown(self) -> None:
        del self.view
        del self.template_names

    abc_data = lambda: (
        ([0, "abc"],),
        ([1, "def"],),
        ([2, "ghi"],),
        ([3, "jkl"],),
    )

    @mock.patch("rent_car.views.reverse")
    def test_success_url(self, reverse):
        reverse.return_value = "abc"
        self.assertEqual("abc", self.view.get_success_url())

    @data_provider(abc_data)
    def test_abc(self, test_case):
        self.view.get_template_names = lambda: self.template_names
        self.assertEqual(test_case[1], self.view.abc(test_case[0]))
