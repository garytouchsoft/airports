from django.db import models


class Airport(models.Model):
    name = models.CharField(max_length=60)
    icao = models.CharField(max_length=60)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, default = 0)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, default = 0)
    
    def __str__(self):
        return self.name
        
