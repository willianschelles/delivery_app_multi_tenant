from django.db import models

from location.models import Location
from driver.models import Driver

class Shipment(models.Model):
     origin = models.ForeignKey(Location, on_delete=models.CASCADE)
     driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
     completion = models.DateTimeField()