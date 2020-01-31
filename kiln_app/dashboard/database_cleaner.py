import os
# this just deletes all data older than seven days
# I run this every day with heroku scheduler

# this setup is required for this script to access djangos ORM
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "kiln_app.settings")
import django
django.setup()

from dashboard.models import *
readings = Reading.objects.all()
from django.utils import timezone
now = timezone.now()
from datetime import timedelta
seven_days = timedelta(days=7)
to_old = now - seven_days

to_delete = readings.filter(timestamp__lt=to_old)

to_delete.delete()
