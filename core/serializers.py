from rest_framework import serializers
from .models import GpsPoint,Data, Journey

class GpsPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = GpsPoint
        fields = ['latitude', 'longitude', 'timestamp']
        # fields = '__all__'

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        # fields = ['cid', 'message']
        fields = '__all__'



class JourneySerializer(serializers.ModelSerializer):
    class Meta:
        model = Journey
        # fields = ['start_point', 'end_point', 'start_time', 'end_time', 'total_distance']
        fields = '__all__'