from django.contrib import admin

# Register your models here.

from .models import BmiMeasurement

admin.site.register(BmiMeasurement)
