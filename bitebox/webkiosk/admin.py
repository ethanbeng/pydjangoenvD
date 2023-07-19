from django.contrib import admin
from .models import Customer, Food, Order, CustomerOrder

# Register your models here.
admin.site.register([Customer, Food, Order, CustomerOrder])