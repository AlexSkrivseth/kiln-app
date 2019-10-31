from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from datetime import datetime, timedelta, timezone
import requests
from dashboard.models import Reading, Load, Kiln
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

    try:
        # gather latest reading from each kiln load
        kiln1_readings = Reading.objects.filter(load__kiln=1)
        reading1 = kiln1_readings.latest('timestamp')
        kiln2_readings = Reading.objects.filter(load__kiln=2)
        reading2 = kiln2_readings.latest('timestamp')

        loads = Load.objects.filter(active=True)
        load1 = loads.get(kiln=1)
        load2 = loads.get(kiln=2)
        daynum1 = (datetime.now(timezone.utc) - load1.startdate).days
        daynum2 = (datetime.now(timezone.utc) - load2.startdate).days
        # do some calculations with the temperature and the humidity
        # to get the absolute humidity in the kiln
        # absolute_humidity is in the api.utils file
        kiln1ah = absolute_humidity(t=reading1.temperature, rh=reading1.humidity)
        kiln2ah = absolute_humidity(t=reading2.temperature, rh=reading2.humidity)

        # Do some logic here to see how the kilns are trending.
        # eg  trend = Reading.NOW - READING.24hoursPAST
        #trend = {'kiln1':{'temp': }}
                                        # could make this dynamic
        old_timestamp1 = reading1.timestamp - timedelta(days=1)
        old_timestamp2 = reading2.timestamp - timedelta(days=1)

        old_reading1_set = kiln1_readings.filter(timestamp__lt=old_timestamp1)

        old_reading2_set = kiln2_readings.filter(timestamp__lt=old_timestamp2)
        old_reading1 = old_reading1_set.latest('timestamp')
        old_reading2 = old_reading2_set.latest('timestamp')

        old_kiln1ah = absolute_humidity(t=old_reading1.temperature, rh=old_reading1.humidity)
        old_kiln2ah = absolute_humidity(t=old_reading2.temperature, rh=old_reading2.humidity)

        trend = {
            'kiln1':{
                'temperature': round(reading1.temperature - old_reading1.temperature, 2),
                'humidity': round(reading1.humidity - old_reading1.humidity, 2),
                'ahumidity': round(kiln1ah - old_kiln1ah, 2),
            },
            'kiln2':{
                'temperature': round(reading2.temperature - old_reading2.temperature, 2),
                'humidity': round(reading2.humidity - old_reading2.humidity, 2),
                'ahumidity': round(kiln2ah - old_kiln2ah, 2),
            },

        }


        # pass the readings as context
        context = {
                    'reading1': reading1,
                    'reading2': reading2,
                    'current_conditions': current_conditions,
                    'ah1': kiln1ah,
                    'ah2': kiln2ah,
                    'trend': trend,
                    'daynum1': daynum1,
                    'daynum2': daynum2,
          }
        return render(request, 'dashboard/main.html', context=context)
    except Exception as e:
        return HttpResponse("Fail {}".format(e))

# a detail page for each kiln
# make custom querys
# look back on historical data
#
def kiln(request, kiln_id):
    if kiln_id == 1 or kiln_id == 2:
        # need to load the temps of kiln-2 into a list
        readings = Reading.objects.filter(load__kiln=kiln_id)
        readings = readings.filter(timestamp__gte=datetime.now() - timedelta(days=15))
        context = {
                'temps':[int(reading.temperature) for reading in readings],
                'humids': [int(reading.humidity) for reading in readings],
                'time': [str(reading.timestamp) for reading in readings]
        }
        print(context)
        return render(request, 'dashboard/test.html', context=context)
    else:
        return HttpResponse('No kiln with that ID try 1 or 2')
