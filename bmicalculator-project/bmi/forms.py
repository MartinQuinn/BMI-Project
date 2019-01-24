# Martin Quinn 24-01-2019
# PTA18070

from django import forms
from bmi.models import BmiMeasurement
import datetime

class BmiForm(forms.Form):
    """
    height is in meters
    weight is in kg
    """
    name = forms.CharField(max_length=255, required=False)
    height = forms.FloatField(label="Height in centimeters:", required=True, min_value=0)
    weight = forms.FloatField(label="Weight in kg:", required=True, min_value=0)

class BmiMeasurementForm(forms.ModelForm):
    class Meta:
        model = BmiMeasurement
        fields = ["id", "name", "height_in_centimeters", "weight_in_kg"]
