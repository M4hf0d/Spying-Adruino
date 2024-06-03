from rest_framework import serializers
from .models import GpsPoint,Data, Journey

class GpsPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = GpsPoint
        # fields = ['id','latitude', 'longitude', 'timestamp']
        exclude = ['journey']

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        # fields = ['cid', 'message']
        fields = '__all__'



class JourneySerializer(serializers.ModelSerializer):
    gps_points = GpsPointSerializer(many=True, read_only=True)
    class Meta:
        model = Journey
        # fields = ['start_point', 'end_point', 'start_time', 'end_time', 'total_distance']
        fields = '__all__'
        depth = 1