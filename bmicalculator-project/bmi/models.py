# Martin Quinn 24-01-2019
# PTA18070


from django.db import models
from datetime import datetime
# Create your models here.

class BmiMeasurement(models.Model):
    name = models.CharField(max_length=255)
    height_in_centimeters = models.FloatField()
    weight_in_kg = models.FloatField()
    measured_at = models.DateTimeField('date created', default=datetime.now)

    def bmi(self):
        return round(((self.weight_in_kg / self.height_in_centimeters ** 2)*10000) , 2)
