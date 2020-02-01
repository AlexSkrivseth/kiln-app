# kiln-app
a django web app I am building as a final project for rmotr

# Compenents of this app

Two raspberry pi's with dht22 temperature and humidity sensors on them.

  - each pi runs a python script that first collects the data and
  then makes a POST request to the app using the requests library
  - the script you can find here "kiln_app/api/piscript.py"
  - you will need to the set script up to run off the crontab
    at the time interval that you want. I do every 10 minutes


A web application built with django hosted on heroku
  - an api built with the django_rest_framework
  - a dashboard app to display the the latest data


#commands to get the app running
set the PythonPath and the settings module

export PYTHONPATH=kiln_app DJANGO_SETTINGS_MODULE=kiln_app.settings.dev
