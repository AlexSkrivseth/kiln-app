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

    # def validate(self, data):
    #     kiln1_loads = Load.objects.filter(kiln=1)
    #     kiln2_loads = Load.objects.filter(kiln=2)
    #
    #     active_loads = kiln1_loads.filter(enddate=None)
    #
    #
    #     if len(active_loads) == 2:
    #
    #         if active_loads[0].startdate > active_loads[1].startdate:
    #             active_loads[1].enddate = datetime.datetime.now()
    #             active_loads[1].active = False
    #             active_loads[1].save()
    #         else:
    #             active_loads[0].enddate = datetime.datetime.now()
    #             active_loads[0].active = False
    #             active_loads[0].save()
    #
    #     if len(active_loads) > 2:
    #         print('you got issues in your db man. Check out the admin page to fix them.')
    #
    #
    #
    #     active_loads2 = kiln2_loads.filter(enddate=None)
    #
    #     if len(active_loads2) == 2:
    #         if active_loads2[0].startdate > active_loads2[1].startdate:
    #             active_loads2[1].enddate = datetime.datetime.now()
    #             active_loads2[1].active = False
    #             active_loads2[1].save()
    #         else:
    #             active_loads2[0].enddate = datetime.datetime.now()
    #             active_loads2[0].active = False
    #             active_loads2[0].save()
