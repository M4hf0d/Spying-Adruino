from django.db import models

class GPSData(models.Model):
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    timestamp = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f'{self.latitude}, {self.longitude}'
    

class Data(models.Model):
    id = models.IntegerField(default=0, blank = True, null = True)
    message = models.TextField(max_length=900, blank = True, null = True)