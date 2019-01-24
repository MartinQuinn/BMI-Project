# Martin Quinn 24-01-2019
# PTA18070

from django.urls import reverse
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from bmi.forms import BmiForm, BmiMeasurementForm
from bmi.models import BmiMeasurement
from django.core.paginator import Paginator

# Create your views here.

def greeting_view(request):
    return render(request, "greeting.html")

def measurement(request, id):
    if request.method == "POST":
        get_object_or_404(BmiMeasurement, pk=id).delete()
        # BmiMeasurement.objects.get(id="id").delete()
        return redirect(reverse("all_measurements"))

def measurements(request):
    measurements = BmiMeasurement.objects.order_by("-measured_at").all()
    paginator = Paginator(measurements, 15)
    page = request.GET.get('page')
    mesurements_pages = paginator.get_page(page)
    return render(request, "measurements.html", {"measurements": mesurements_pages})

def bmi(request):
    if request.method == "POST":
        form = BmiForm(request.POST)
        if form.is_valid():
            height = form.cleaned_data["height"]
            weight = form.cleaned_data["weight"]
            bmi = (weight/height*2)
            return render(request, "bmi.html", {"form": form, "bmi": bmi})
    else:
        form = BmiForm()
    return render(request, "bmi.html", {"form": form})

def bmi_measurement(request):
    if request.method == "POST":
        form = BmiMeasurementForm(request.POST)
        if form.is_valid():
            measurement = form.save()
            measurements = BmiMeasurement.objects.order_by("-measured_at").all()
            paginator = Paginator(measurements, 15)
            page = request.GET.get('page')
            mesurements_pages = paginator.get_page(page)
            return render(request, "measurement_recorded.html", {"measurements": measurements_pages})
    else:
        measurements = BmiMeasurement.objects.order_by("-measured_at").all()
        paginator = Paginator(measurements, 15)
        page = request.GET.get('page')
        mesurements_pages = paginator.get_page(page)
        form = BmiMeasurementForm()
    return render(request, "measurement.html", {"form": form, "measurements": measurements_pages})
