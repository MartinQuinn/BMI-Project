from django.db import models
from datetime import datetime
# Create your models here.

class BmiMeasurement(models.Model):
    height_in_meters = models.FloatField()
    weight_in_kg = models.FloatField()
    measured_at = models.DateTimeField('date created', default=datetime.now)

    def bmi(self):
        return round(((self.weight_in_kg / self.height_in_meters ** 2)*10000) , 2)
