from datetime import timezone
from django.db import models

class GpsPoint(models.Model):
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    timestamp = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f'{self.latitude}, {self.longitude}'
    def save(self, *args, **kwargs):
        if self.timestamp is None:
            self.timestamp = timezone.now()
        super().save(*args, **kwargs)

class Data(models.Model):
    cid = models.IntegerField(default=0, blank = True, null = True)
    message = models.TextField(max_length=900, blank = True, null = True)
    def __str__(self) :
        return f'{self.cid}, {self.message}'