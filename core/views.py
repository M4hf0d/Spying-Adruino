from rest_framework import viewsets, status
from rest_framework.filters import OrderingFilter
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from .models import GpsPoint, Data, Journey
from .serializers import GpsPointSerializer, DataSerializer,JourneySerializer
from datetime import timedelta,datetime,timezone
from django_admin_geomap import geomap_context
from django.shortcuts import render
from . models import *

class JourneyViewSet(viewsets.ModelViewSet):
    queryset = Journey.objects.all()
    serializer_class = JourneySerializer
    filter_backends = [OrderingFilter]
    ordering_fields = ['id', 'total_distance','start_time','average_speed','end_point']   


class LastGpsPointView(ListAPIView):
    serializer_class = GpsPointSerializer

    def get_queryset(self):
        # Get the last GPS point
        last_point = GpsPoint.objects.order_by('-timestamp').first()

        # Return a queryset containing only the last GPS point
        return GpsPoint.objects.filter(id=last_point.id) if last_point else GpsPoint.objects.none()

class GpsPointViewSet(viewsets.ModelViewSet):
    queryset = GpsPoint.objects.all()
    serializer_class = GpsPointSerializer
    filter_backends = [OrderingFilter]
    ordering_fields = ['timestamp' , 'id']     

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Get the last GPS point
        last_point = GpsPoint.objects.order_by('timestamp').last()

        # Get the current time
        # now = datetime.now(timezone.utc) + timedelta(hours=2)

        # changed spot after 20 mins start a new journey & end last one if exists
        if (not last_point) or ( serializer.validated_data['timestamp'] - last_point.timestamp > timedelta(minutes=20) and ( last_point.latitude != serializer.validated_data['latitude'] and last_point.longitude != serializer.validated_data['longitude'])):
            open_journey = Journey.objects.order_by('-id').first()
            if  open_journey and not open_journey.end_point:
                journey = Journey.objects.order_by('-id').first()
                journey.end_point = last_point
                journey.end_time = last_point.timestamp
                journey.calculate_stats()
                journey.save()
                print(" Closed Last")
                
            gps_point = GpsPoint.objects.create(**serializer.validated_data)
            journey = Journey.objects.create(start_point=gps_point, start_time=gps_point.timestamp)
            gps_point.journey = journey
            print(" # changed spot after 20 mins start a new journey")
            gps_point.save()
        # Same Spot for more than 20 mins end the journey
        elif serializer.validated_data['timestamp'] - last_point.timestamp > timedelta(minutes=20):
            journey = Journey.objects.order_by('-id').first() 
            gps_point = GpsPoint.objects.create(**serializer.validated_data, journey=journey)
            journey.end_point = gps_point  # Set end_point to the current GpsPoint
            journey.end_time = gps_point.timestamp
            journey.calculate_stats()
            journey.save()
            gps_point.save()
            print("Same Spot for more than 20 mins end the journey")
        # Otherwise, get the current journey and append
        else:
            journey = Journey.objects.order_by('-id').first()
            gps_point = GpsPoint.objects.create(**serializer.validated_data, journey=journey)
            gps_point.save()
            print("   # Otherwise, get the current journey and append")

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
# TODO: Signal to calculate distance and time for the journey ...ect
class DataViewSet(viewsets.ModelViewSet):
    queryset = Data.objects.all()
    serializer_class = DataSerializer




def home(request):
    return render(request, 'core/home.html', geomap_context(GpsPoint.objects.all() ,auto_zoom="10"))