#!/usr/bin/env python3
# this script is meant to act as a client on a raspberry pi
import json
import Adafruit_DHT as dht
import datetime
import requests
import time

# this script runs every 10 minutes from the crontab
def celcius_farenheit(x):
    f = (x * 1.8) + 32
    return f

def read_sensor():
    h,t = dht.read_retry(dht.DHT22, 4)

    temp = str(round(celcius_farenheit(t),2))
    humid = str(round(h,2))

    return temp, humid

def post():

    t, h = read_sensor()
    reading = {'temperature': t, 'humidity': h}

    #sending a post request to the api
    url_endpoint = 'https://wherever_the_app_is_hosted'
    requests.post(url_endpoint, json=reading, headers={
        # both pis can use this Token
        'Authorization': 'Token 90c7e49e8adebad43e7a900fbcf5936a75a5db3e',
        # this is a custom header that the kiln-app must have to create a new reading
        # this must be '1' or '2' depending on which pi this script is on.
        'kiln': '1'}
                  )

def main():
    try:
        post()
    except Exception as e:
        print(e)

main()
