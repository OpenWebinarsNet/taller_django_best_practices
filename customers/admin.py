from django.contrib import admin

# Register your models here.
from django.contrib.admin import ModelAdmin

from customers.models import Customer


@admin.register(Customer)
class CustomerAdmin(ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email')
