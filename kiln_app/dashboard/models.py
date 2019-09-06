from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    email = models.EmailField(max_length=254, blank=True)

class Load(models.Model):
    fiber = models.FileField(upload_to='uploaded_files/', blank=True)
    job = models.CharField(max_length=30, blank=True)
    startdate = models.DateTimeField(auto_now_add=True)
    enddate = models.DateTimeField(blank=True, null=True)
    loadnumber = models.PositiveSmallIntegerField(blank=True)
    kiln = models.ForeignKey('Kiln', on_delete=models.CASCADE)

class Reading(models.Model):
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    humidity = models.DecimalField(max_digits=5, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    load = models.ForeignKey(Load, on_delete=models.CASCADE)



class Kiln(models.Model):
    active = models.BooleanField(True)
    name = models.CharField(max_length=10, default='Kiln-1')




# future plans for this.
# class Report(models.Model):
#     startdate = models.DateTimeField(editable=True)
#     enddate = models.DateTimeField(editable=True)
#     report = models.FileField()




# having trouble figuring out the one to many relationship and all.
# any place I used ForeignKey, im not sure if i used it correctly.
