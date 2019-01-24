# Martin Quinn 24-01-2019
# PTA18070

from django.contrib import admin

# Register your models here.

from .models import BmiMeasurement

admin.site.register(BmiMeasurement)
