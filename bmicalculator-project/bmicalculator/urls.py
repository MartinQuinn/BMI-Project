"""bmicalculator URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# Martin Quinn 24-01-2019
# PTA18070


from django.conf.urls import url
from django.contrib import admin
from bmi import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.bmi_measurement),
    url(r'^bmi/$', views.bmi_measurement),
    url(r'^measurement/$', views.bmi_measurement),
    url(r'^measurements/$', views.measurements, name="all_measurements"),
    url(r'^measurements/(?P<id>\d+)/$', views.measurement, name="delete_measurement"),
]
