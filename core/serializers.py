from rest_framework import serializers
from .models import GPSData,Data

class GPSDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = GPSData
        # fields = ['latitude', 'longitude', 'timestamp']
        fields = '__all__'

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        # fields = ['cid', 'message']
        fields = '__all__'
