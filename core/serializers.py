from rest_framework import serializers
from .models import GpsPoint,Data

class GpsPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = GpsPoint
        # fields = ['latitude', 'longitude', 'timestamp']
        fields = '__all__'

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        # fields = ['cid', 'message']
        fields = '__all__'
