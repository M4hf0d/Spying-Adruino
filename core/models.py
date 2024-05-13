from datetime import timedelta, timezone
from django.db import models
from geopy.distance import geodesic
from django_admin_geomap import GeoItem

class GpsPoint(models.Model , GeoItem):
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    timestamp = models.DateTimeField(blank=True, null=True)
    journey = models.ForeignKey('Journey', on_delete=models.CASCADE, related_name='gps_points', blank=True, null=True)
    speed = models.DecimalField(max_digits= 6 , decimal_places=2, null = True, blank = True)
    heading = models.DecimalField(max_digits= 10 , decimal_places=2, null = True, blank = True)
    def __str__(self):
        return f'{self.latitude}, {self.longitude}'
    
    def save(self, *args, **kwargs):
        if self.timestamp is None:
            self.timestamp = timezone.now()
        super().save(*args, **kwargs)
    @property
    def geomap_longitude(self):
        return '' if self.longitude is None else str(self.longitude)

    @property
    def geomap_latitude(self):
        return '' if self.latitude is None else str(self.latitude)

    @property
    def geomap_popup_view(self):
        return f"<strong>{self.journey.id} <br> {self.speed} </strong>".format(str(self))

    @property
    def geomap_popup_edit(self):
        return self.geomap_popup_view

    @property
    def geomap_popup_common(self):
        return self.geomap_popup_view


class Data(models.Model):
    cid = models.IntegerField(default=0, blank = True, null = True)
    message = models.TextField(max_length=900, blank = True, null = True)
    def __str__(self) :
        return f'{self.cid}, {self.message}'
    
class Journey(models.Model):
    start_point = models.ForeignKey(GpsPoint, related_name='start_journeys', on_delete=models.CASCADE)
    end_point = models.ForeignKey(GpsPoint, related_name='end_journeys', on_delete=models.CASCADE, blank=True, null=True)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(blank=True, null=True)
    total_distance = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)  # in meters
    average_speed = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)  # in km/h
    duration = models.DurationField(blank=True, null=True)  # in seconds
    max_speed = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)  # in km/h

    def __str__(self):
        return f'Journey {self.id} @ {self.start_time} '
    
    def calculate_stats(self):
        gps_points = self.gps_points.order_by('timestamp')
        total_distance = 0.0
        max_speed = 0.0
        previous_point = None
        previous_time = None
        average_speed = 0.0  # Initialize average speed

        for gps_point in gps_points:
            if previous_point is not None:
                distance = geodesic(previous_point, (gps_point.latitude, gps_point.longitude)).meters
                total_distance += distance
                time_difference = (gps_point.timestamp - previous_time).total_seconds() / 3600  # in hours
                if time_difference > 0:  # avoid division by zero
                    speed = gps_point.speed
                    max_speed = max(max_speed, speed)
                    average_speed += speed  # Accumulate speed for average calculation

            previous_point = (gps_point.latitude, gps_point.longitude)
            previous_time = gps_point.timestamp

        self.total_distance = total_distance
        self.duration = self.end_time - self.start_time if self.end_time else timedelta(seconds=0)
        self.average_speed = average_speed / len(gps_points) if len(gps_points) > 0 else 0 
        self.max_speed = max_speed