from django.contrib import admin

from customer.models import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("username", "first_name", "last_name", "is_staff", "is_active", "date_joined")
