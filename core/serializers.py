from rest_framework import serializers
from .models import GPSData

class GPSDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = GPSData
        fields = ['latitude', 'longitude', 'timestamp']