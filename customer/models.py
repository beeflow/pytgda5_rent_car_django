from django.contrib.auth.models import AbstractUser

from django.db import models

from django.utils.translation import gettext_lazy as _


class Customer(AbstractUser):
    customer_number = models.CharField(verbose_name=_("Number"), max_length=6)

    class Meta:
        verbose_name_plural = _("Customers")
        verbose_name = _("Customer")

    def __str__(self):
        return f"{self.get_full_name()} ({self.username})"
