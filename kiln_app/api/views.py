from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from api.utils import end_load # to enforce rules
from dashboard.models import Reading, Load
from api.serializers import ReadingSerializer, LoadSerializer

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action



# YOUR VIEWS HERE

class ReadingModelViewSet(viewsets.ModelViewSet):
    serializer_class = ReadingSerializer
    queryset = Reading.objects.all()


class LoadModelViewSet(viewsets.ModelViewSet):
    serializer_class = LoadSerializer
    queryset = Load.objects.all()
    # this line will not get executed everytime, and I dont know why?
    
    end_load()



    def retrieve(self, request, pk):
        instance = self.get_object()
        serializer = self.get_serializer(instance)


        return Response(serializer.data)





    # include logic to:
    # when a new load is created give the old load an endate
    # check that there is only one load active for each kiln.
    # that the load that is active is the latest load




        # gather loads with no enddate should only be two at most
        # take the load with the older startdate and give it an enddate of now
        # call the is_active method on that load which shoud switch it off.
