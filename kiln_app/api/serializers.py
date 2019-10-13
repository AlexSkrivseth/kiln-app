from rest_framework import serializers
import datetime

from dashboard.models import Reading, Load, Kiln


class ReadingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reading
        fields = ['id','temperature', 'humidity', 'timestamp', 'load']


class LoadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Load
        fields = ['id','fiber', 'job', 'startdate', 'enddate', 'kiln', 'active']

    
