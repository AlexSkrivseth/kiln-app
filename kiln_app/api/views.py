from django.shortcuts import render

# Create your views here.

from dashboard.models import Reading
# create this serializers
from api.serializers import ReadingSerializer
# import the rest_framework
from rest_framework import viewsets




# YOUR VIEWS HERE

class ReadingModelViewSet(viewsets.ModelViewSet):
    serializer_class = ReadingSerializer
    queryset = Reading.objects.all()
