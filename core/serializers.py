from rest_framework import serializers
from .models import GPSData,Data

class GPSDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = GPSData
        fields = ['latitude', 'longitude', 'timestamp']

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = ['id', 'message']