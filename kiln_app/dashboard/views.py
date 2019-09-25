from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import datetime
import requests
from dashboard.models import Reading
from api.utils import  absolute_humidity


# Create your views here.

# index provides a broad overview of current conditions
def index(request):
    # hit the darksky api and get the current conditions
    r = requests.get('https://api.darksky.net/forecast/be0d42628d574bdbab49edeaa13d3759/48.721625,-116.303509')
    data = r.json()
    current_conditions = {
    'outside_temp': data['currently']['temperature'],
    'outside_humid': 100 * data['currently']['humidity'],
    'atmospheric_pressure':data['currently']['pressure']
    }
    # Do some logic here to see how the kilns are trending.
    # eg  trend = Reading.NOW - READING.24hoursPAST
    #trend = {'kiln1':{'temp': }}

    # gather latest reading from each kiln load
    kiln1_readings = Reading.objects.filter(load__kiln=1)
    reading1 = kiln1_readings.latest('timestamp')
    kiln2_readings = Reading.objects.filter(load__kiln=2)
    reading2 = kiln2_readings.latest('timestamp')



    # do some calculations with the temperature and the humidity
    # to get the absolute humidity in the kiln
    # absolute_humidity is in the api.utils file
    kiln1ah = absolute_humidity(t=reading1.temperature, rh=reading1.humidity)
    kiln2ah = absolute_humidity(t=reading2.temperature, rh=reading2.humidity)

    # pass the readings as context
    context = {
                'reading1': reading1,
                'reading2': reading2,
                'current_conditions': current_conditions,
                'ah1': kiln1ah,
                'ah2': kiln2ah,
      }
    return render(request, 'dashboard/main.html', context=context)

# a detail page for each kiln
# make custom querys
# look back on historical data
#
def kiln(request, kiln_id):
    return render(request, 'dashboard/base.html')
