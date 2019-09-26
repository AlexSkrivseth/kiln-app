from dashboard.models import Load, Kiln
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
            active_loads[1].enddate = datetime.datetime.now()
            active_loads[1].active = False
            active_loads[1].save()
        else:
            active_loads[0].enddate = datetime.datetime.now()
            active_loads[0].active = False
            active_loads[0].save()

    if len(active_loads) > 2:
        print('you got issues in your db man. Check out the admin page to fix them.')



    active_loads2 = kiln2_loads.filter(enddate=None)

    if len(active_loads2) == 2:
        if active_loads2[0].startdate > active_loads2[1].startdate:
            active_loads2[1].enddate = datetime.datetime.now()
            active_loads2[1].active = False
            active_loads2[1].save()
        else:
            active_loads2[0].enddate = datetime.datetime.now()
            active_loads2[0].active = False
            active_loads2[0].save()

    if len(active_loads2) > 2:
        # raise exception here
        print('you got issues in your db man. Check out the admin page to fix them.')
        print('you have too many loads active')

    # print('\n')
    # print('end_load was called')
    # print('\n')
    return None



def _get_active_load(kiln_id):
    loads = Load.objects.filter(kiln__id=kiln_id)
    try:
        active_load = loads.get(active=True)
    except:
        #raise excpetion here
        print('\n')
        print('Got an error Dude')
        print('\n')
    return active_load.id

# pass in Temp in farhenheit
def absolute_humidity(t=None, rh=None):
    t = int(t)
    rh = int(rh)
    if t and rh:
        T = (t - 32) * 5/9
        # T is celsius
        ah = 6.112 * 2.71828**((17.67 * T)/(T+243.5)) * rh * 2.1674 / (273.15+T)
        AH = round(ah, 2)
        print("The absolute_humidity is {} grams/m3".format(ah))

        return AH
    else:
        return "Please give two keyword arguments eg. (t=89,rh=67)"
