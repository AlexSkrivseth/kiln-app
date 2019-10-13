from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from api.utils import _get_active_load, end_load

from dashboard.models import Reading, Load
from api.serializers import ReadingSerializer, LoadSerializer

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action


# YOUR VIEWS HERE
class ReadingModelViewSet(viewsets.ModelViewSet):
    serializer_class = ReadingSerializer
    queryset = Reading.objects.all()
    # overwriting this function to add some cusomization
    def create(self, request, *args, **kwargs):
        # adding the correct load number to the reading before it goes to the serializer
        request.data['load'] = _get_active_load(request.headers['kiln'])
        #
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class LoadModelViewSet(viewsets.ModelViewSet):
    serializer_class = LoadSerializer
    queryset = Load.objects.all()


    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        # custom logic here to end the previous load.
        queryset = Load.objects.all()
        if len(queryset) >= 3:
            end_load()
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

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
