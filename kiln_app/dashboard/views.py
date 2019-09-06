from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('You made it!')


def kiln(request, kiln_id):
    return HttpResponse('You are looking at kiln_{} '.format(kiln_id))

def change_load(request, kiln_id):
    return HttpResponse('You are looking at kiln_{} '.format(kiln_id))

def create_report(request, kiln_id):
    return HttpResponse('You are looking at kiln_{} '.format(kiln_id))
