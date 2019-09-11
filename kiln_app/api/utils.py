from dashboard.models import Load
import datetime

# call this to enforce the rule:
# one load per kiln can be active
# gives the old load an enddate

def end_load():

    kiln1_loads = Load.objects.filter(kiln=1)
    kiln2_loads = Load.objects.filter(kiln=2)

    active_loads = kiln1_loads.filter(enddate=None)


    if len(active_loads) == 2:

        if active_loads[0].startdate > active_loads[1].startdate:
            print('changing index2')
            active_loads[1].enddate = datetime.datetime.now()
            active_loads[1].active = False
            active_loads[1].save()
        else:
            print('changing index1')
            active_loads[0].enddate = datetime.datetime.now()
            active_loads[0].active = False
            active_loads[0].save()



    active_loads2 = kiln2_loads.filter(enddate=None)

    if len(active_loads) == 2:
        if active_loads2[0].startdate > active_loads[1].startdate:
            print('changing index2')
            active_loads2[1].enddate = datetime.datetime.now()
            active_loads2[1].active = False
            active_loads2[1].save()
        else:
            print('changing index1')
            active_loads2[0].enddate = datetime.datetime.now()
            active_loads2[0].active = False
            active_loads2[0].save()
    print('DNAG')
    return None
