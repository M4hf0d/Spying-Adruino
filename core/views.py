from rest_framework import generics, viewsets, filters
from rest_framework.filters import OrderingFilter
from .models import GpsPoint, Data
from .serializers import GpsPointSerializer, DataSerializer

class GpsPointViewSet(viewsets.ModelViewSet):
    queryset = GpsPoint.objects.all()
    serializer_class = GpsPointSerializer
    filter_backends = [OrderingFilter]
    ordering_fields = ['timestamp']     
    
class DataViewSet(viewsets.ModelViewSet):
    queryset = Data.objects.all()
    serializer_class = DataSerializer